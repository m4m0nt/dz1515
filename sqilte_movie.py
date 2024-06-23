from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///movies_db.db')
Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    year = Column(Integer)
    genre = Column(String)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

movies = [
    Movie(title="Interstellar", director="Christopher Nolan", year=2014, genre="Sci-Fi"),
    Movie(title="The Lord of The Rings", director="Peter Jackson", year=2003, genre="Fantasy"),
    Movie(title="Pulp Fiction", director="Quentin Tarantino", year=1994, genre="Crime"),
    Movie(title="Dune", director="Denis Villeneuve", year=2021, genre="Sci-Fi"),
    Movie(title="The Godfather", director="Francis Ford Coppola", year=1972, genre="Crime")
]

session.add_all(movies)
session.commit()

director_name = "Christopher Nolan"
movies_by_director = session.query(Movie).filter(Movie.director == director_name).all()
print(f"Movies directed by {director_name}:")
for movie in movies_by_director:
    print(movie.title)

movie_to_update = session.query(Movie).filter(Movie.title == "The Lord of The Rings").first()
if movie_to_update:
    movie_to_update.year = 2002
    session.commit()

movie_to_delete = session.query(Movie).filter(Movie.title == "Pulp Fiction").first()
if movie_to_delete:
    session.delete(movie_to_delete)
    session.commit()

all_movies = session.query(Movie).all()
print("All movies")
for movie in all_movies:
    print(f"{movie.title}, directed by {movie.director}, year {movie.year}, genre {movie.genre}")

session.close()
