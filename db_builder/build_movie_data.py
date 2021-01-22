import os
from pathlib import Path
from tqdm import tqdm
import django

BASE_DIR = Path(__file__).resolve().parent.parent
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recoflix_project.settings')


django.setup()

from recoflix.models import Movie, Genre

movie_data_path = os.path.join(BASE_DIR, 'resources/MovieTweetings/movies.dat')


def create_movie(movie_id, title, genres):
    movie = Movie.objects.get_or_create(movie_id=movie_id)[0]

    title_and_year = title.split(sep="(")

    movie.title = title_and_year[0]
    movie.year = title_and_year[1][:-1]

    if genres:
        for genre in genres.split(sep="|"):
            g = Genre.objects.get_or_create(name=genre)[0]
            movie.genres.add(g)
            g.save()

    movie.save()

    return movie


def delete_db():
    print('Truncate movie db')
    movie_count = Movie.objects.all().count()

    if movie_count > 1:
        Movie.objects.all().delete()
        Genre.objects.all().delete()
    print('Finished truncate db')


def populate():
    with open(movie_data_path, 'rt') as f:
        movies = f.readlines()
        for movie in tqdm(movies):
            m = movie.strip().split(sep="::")
            if len(m) == 3:
                create_movie(*m)


if __name__ == '__main__':
    print("Starting building RecoFlix movie data script...")
    delete_db()
    populate()
