import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')

django.setup()
from firstapp.models import User

from faker import Faker
fakegen = Faker()

for i in range(15):
    fake_name = fakegen.name().split()
    fake_fname = fake_name[0]
    fake_lname = fake_name[1]
    fake_email = fakegen.email()
    user = User.objects.get_or_create(fname=fake_fname, lname=fake_lname, email=fake_email)[0]
    user.save()
