from flask import Flask, render_template, request, redirect, url_for
from data_manager import DataManager
from models import db, Movie
import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv('API_KEY')

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/movies.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

data_manager = DataManager()

@app.route('/')
def index():
    users = data_manager.get_users()
    return render_template('index.html', users=users)

@app.route('/users', methods=['POST'])
def create_user():
    name = request.form.get('name')
    if name.strip() == "":
        return "Name is empty"
    else:
        data_manager.create_user(name)
        return redirect(url_for('index'))

@app.route('/users/<int:user_id>/movies')
def get_movies(user_id):
    movies = data_manager.get_movies(user_id)
    return render_template('movies.html', movies=movies, user_id=user_id)

@app.route('/users/<int:user_id>/movies', methods=['POST'])
def add_movie(user_id):
    user = data_manager.get_user(user_id)
    if user is None:
        return "User not found", 404

    title = request.form.get('name')
    try:
        response = requests.get(f"http://www.omdbapi.com/?t={title}&apikey={api_key}")
        data = response.json()
    except Exception as e:
        return "Could not reach movie database", 500

    if data['Response'] == 'False':
        return render_template('404.html'), 404

    movie = Movie(
        name=data['Title'],
        director=data['Director'],
        year=data['Year'],
        poster_url=data['Poster'],
        user_id=user_id
    )
    data_manager.add_movie(movie)
    return redirect(url_for('get_movies', user_id=user_id))

@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie(user_id, movie_id):
    title = request.form.get('title')
    director = request.form.get('director')
    year = request.form.get('year')
    data_manager.update_movie(movie_id, title, director, year)
    return redirect(url_for('get_movies', user_id=user_id))

@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_movie(user_id, movie_id):
    data_manager.delete_movie(movie_id)
    return redirect(url_for('get_movies', user_id=user_id))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
  with app.app_context():
    db.create_all()

  app.run()