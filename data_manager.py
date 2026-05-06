from models import db, User, Movie

class DataManager():
    def create_user(self, name):
        user = User(name=name)
        db.session.add(user)
        db.session.commit()

    def get_users(self):
        users = User.query.all()
        return users

    def get_movies(self, user_id):
        movies = Movie.query.filter_by(user_id=user_id).all()
        return movies

    def add_movie(self, movie):
        db.session.add(movie)
        db.session.commit()

    def update_movie(self, movie_id, new_title):
        movie = Movie.query.get(movie_id)
        movie.name = new_title
        db.session.commit()


    def delete_movie(self, movie_id):
        movie = Movie.query.get(movie_id)
        db.session.delete(movie)
        db.session.commit()