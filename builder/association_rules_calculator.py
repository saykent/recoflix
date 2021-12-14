import os
from datetime import datetime
from collections import defaultdict
from itertools import combinations

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recoflix_project.settings")
django.setup()

from collector.models import Log
from recommender.models import SeededRecs


def build_association_rules():
    data = retrieve_buy_events()
    data = generate_transactions(data)


def retrieve_buy_events():
    data = Log.objects.filter(event='buy').values()
    return data


def generate_transactions(data):
    transactions = defaultdict(list)

    for transaction_item in data:
        transaction_id = transaction_item["session_id"]
        transactions[transaction_id].append(transaction_item["content_id"])

    return transactions


if __name__ == '__main__':
    print("Calculating association rules...")
    build_association_rules()
