from models import db, User, Movie

class DataManager():
    def create_user(self, name):
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def get_users(self):
        all_users = User.query.all()
        return all_users

    def get_movies(self, user_id):
        all_movies = Movie.query.filter_by(user_id=user_id).all()
        return all_movies

    def add_movie(self, movie):
        db.session.add(movie)
        db.session.commit()

    def update_movie(self, movie_id, new_title):
        updated_movie = Movie.query.get(movie_id)
        updated_movie.name = new_title
        db.session.commit()


    def delete_movie(self, movie_id):
        deleted_movie = Movie.query.get(movie_id)
        db.session.delete(deleted_movie)
        db.session.commit()