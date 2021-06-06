import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')

import django
django.setup()
from firstapp.models import Topic,AccessRecord,Webpage

import random
from faker import Faker

fakegen=Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()  #top is an object 
        fake_url = fakegen.url()
        fake_date = fakegen.date(pattern='%Y-%m-%d', end_datetime=None)
        fake_name = fakegen.company()
        
        wpg = Webpage.objects.get_or_create(topics=top, url=fake_url, name=fake_name)[0]
        
        acc_rec = AccessRecord.objects.get_or_create(name=wpg, date=fake_date)
        
if __name__ == '__main__':
    print("Populating script")
    populate(20)
    print("Done")
    


