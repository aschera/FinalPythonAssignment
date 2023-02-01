import requests
from CraftBeerInfoApp.models import Beer
import pandas as pd

# maybe try: https://medium.com/@chilinski.a/how-to-seed-a-django-api-with-data-from-an-external-api-b577b6e6ad54

#  Within your app file, create a management directory with a commands directory inside. Create a seed.py file inside /management/commands/.


class Beer_class:
  

    def __init__(self, beer):
        print("Object created {beer}")

    def get_beers():
      beer = pd.read_json('C:/Users/asche/FinalPythonAssignment/assets/beer_output.json') 
      return beer

    def seed_beer():
        print(Beer)
        for i in get_beers():
          beer = Beer(
            name = i["Name"]
          )
        beer.save()

    def clear_data():
      Beer.objects.all().delete()

