import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")
django.setup()

from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()

topics = ["Search", "Social", "Marketplace", "News", "Games"]


def populate(N=5):
    for entry in range(N):
        # Create the fake data for the entry
        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()

        # Get or create the topic for the entry
        topic = Topic.objects.get_or_create(name=random.choice(topics))[0]

        # Create the new webpage entry
        webpage = Webpage.objects.get_or_create(
            topic=topic, url=fake_url, name=fake_name
        )[0]

        # Create a fake access record for that webpage
        access_record = AccessRecord.objects.get_or_create(
            name=webpage, date=fake_date
        )[0]


if __name__ == "__main__":
    print("Populating script!")
    populate()
    print("Populating complete!")
