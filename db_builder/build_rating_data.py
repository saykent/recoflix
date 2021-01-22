import os
import django
import decimal
from pathlib import Path
from datetime import datetime, timezone
from tqdm import tqdm

BASE_DIR = Path(__file__).resolve().parent.parent
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recoflix_project.settings')

django.setup()

from analytics.models import Rating

rating_data_path = os.path.join(BASE_DIR, 'resources/MovieTweetings/ratings.dat')


def create_rating(user_id, content_id, rating, timestamp):
    rating = Rating(user_id=user_id, movie_id=content_id, rating=decimal.Decimal(rating),
                    rating_timestamp=datetime.fromtimestamp(float(timestamp), tz=timezone.utc))
    rating.save()

    return rating


def delete_db():
    print('truncate db')
    Rating.objects.all().delete()
    print('finished truncate db')


def populate():
    with open(rating_data_path, 'rt') as f:
        ratings = f.readlines()
        for rating in tqdm(ratings):
            r = rating.strip().split(sep="::")
            if len(r) == 4:
                create_rating(*r)


if __name__ == '__main__':
    print("Starting building RecoFlix rating script...")
    delete_db()
    populate()
