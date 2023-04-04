from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<db-user>:<db-password>@localhost/<db-name>'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    genre = db.Column(db.String(), nullable=False)
class MovieRepository:
    def get_all_movies(self):
        return db.session.query(Movie).all()
class MovieRepository:
    def get_movie_by_id(self, movie_id):
        return db.session.query(Movie).filter_by(id=movie_id).first()
class MovieRepository:
    def create_movie(self, movie_data):
        movie = Movie(
            title=movie_data['title'],
            release_date=movie_data['release_date'],
            genre=movie_data['genre']
        )
        db.session.add(movie)
        db.session.commit()
        return movie
class MovieRepository:
    def search_movies(self, search_term):
        return db.session.query(Movie).filter(
            Movie.title.ilike(f'%{search_term}%') |
            Movie.genre.ilike(f'%{search_term}%')
        ).all()

