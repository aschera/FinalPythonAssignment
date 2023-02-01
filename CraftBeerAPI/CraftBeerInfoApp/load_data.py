

# Providing initial data for models
# https://docs.djangoproject.com/en/2.0/howto/initial-data/

# python manage.py dumpdata  > C:/Users/asche/FinalPythonAssignment/assets/beer_output.json

# show the file location, name, and extension
# python manage.py loaddata C:/Users/asche/FinalPythonAssignment/assets/beer_output.json

# make known the file name and extension
# python manage.py loaddata data.json

# indicates the file name
# python manage.py loaddata data

    # for line in df.split('\n'):
     #    a = Beer(
      #       Type = line[0],
       #      Name = line[1],
      #       Nr = line[2],
      #      Country = line[3],
      #       Amount = line[4],
      #       Percentage= line[5],
     #        Price = line[6],
     #        beer_quantity = line[7],
      #       )
      #   a.save()    



# maybe try: https://medium.com/@chilinski.a/how-to-seed-a-django-api-with-data-from-an-external-api-b577b6e6ad54

#  Within your app file, create a management directory with a commands directory inside. Create a seed.py file inside /management/commands/.

import requests
from django.core.management.base import BaseCommand
from models import Beer
import pandas as pd


def get_beers():
  beer = pd.read_json('C:/Users/asche/FinalPythonAssignment/assets/beer_output.json') 
  return beer


def seed_beer():
  for i in get_beers():
    beer = Beer(
      name = i["Name"]
    )
    beer.save()

def clear_data():
  Beer.objects.all().delete()

class Command(BaseCommand):
  def handle(self, *args, **options):
    seed_beer()
    # clear_data()
    print("completed")

    # run in cmd: python manage.py seed
    # check: python manage.py shell     and then    Fish.objects.all()