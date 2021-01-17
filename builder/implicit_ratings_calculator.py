import os
import datetime
from datetime import timezone

import django
from django.db.models import Count

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recoflix_project.settings")
django.setup()

from collections import defaultdict
from collector.models import Log
from analytics.models import Rating


w1 = 100
w2 = 50
w3 = 15


def query_log_for_users():
    return Log.objects.values('user_id').distinct()


def query_aggregated_log_data_for_user(userid):

    user_data = Log.objects.filter(user_id=userid).values('user_id',
                                                          'content_id',
                                                          'event').annotate(count=Count('created'))
    return user_data


def calculate_implicit_ratings_for_user(user_id):

    data = query_aggregated_log_data_for_user(user_id)

    agg_data = defaultdict(lambda: defaultdict(int))
    max_rating = 0

    for row in data:
        content_id = str(row['content_id'])
        agg_data[content_id][row['event']] = row['count']

    ratings = dict()
    for k, v in agg_data.items():
        rating = w1 * v['buy'] + w2 * v['details'] + w3 * v['moreDetails']
        max_rating = max(max_rating, rating)

        ratings[k] = rating

    for content_id in ratings.keys():
        ratings[content_id] = 10 * ratings[content_id] / max_rating

    return ratings


def save_ratings(ratings, user_id, rating_type):
    print("saving ratings for {}".format(user_id))
    i = 0

    for content_id, rating in ratings.items():
        if rating > 0:
            Rating(
                user_id=user_id,
                movie_id=str(content_id),
                rating=rating,
                rating_timestamp=datetime.datetime.now(tz=timezone.utc),
                type=rating_type
            ).save()
            print('{} {}'.format(user_id, str(content_id)))

        i += 1

        if i == 100:
            print('.', end="")
            i = 0


def calculate_ratings():
    rows = query_log_for_users()
    for user in rows:
        userid = user['user_id']
        ratings = calculate_implicit_ratings_for_user(userid)
        save_ratings(ratings, userid, 'implicit')


if __name__ == '__main__':
    print("Calculating implicit ratings...")
    Rating.objects.filter(type='implicit').delete()
    calculate_ratings()
