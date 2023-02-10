
import json

file = 'beer_output2.json'

# Read JSON objects from a file and create a list of model instances
beers = []
with open(file) as f:
    data = json.load(f)
    with open(file, encoding='utf-8', errors='ignore') as json_file:
        data = json.load(json_file)
        one = data[0]

'''
        for item in data:
            beertype = item.get('beertype')
            beername = item.get('beername')
            beerbrewery = item.get('beerbrewery')
            beerNr = item.get('beerNr')
            beerCountry = item.get('beerCountry')
            beerAmount = item.get('beerAmount')
            beerPercentage = item.get('beerPercentage')
            beerPrice = item.get('beerPrice')

            beer = Beer(beertype=beertype,
                        beername=beername,
                        beerbrewery=beerbrewery,
                        beerNr=beerNr,
                        beerCountry=beerCountry,
                        beerAmount=beerAmount,
                        beerPercentage=beerPercentage,
                        beerPrice=beerPrice)
            beer.save()

'''


# Use bulk_create to insert all objects in one go
# Beer.objects.bulk_create(beers)

# ------------------------------# 

from django.core.management.base import BaseCommand
import json


class Command(BaseCommand):
    help = 'Load beer data from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='The JSON file to load')

    def handle(self, *args, **kwargs):
        file = kwargs['file']

        with open(file) as json_file:
            data = json.load(json_file)

            for item in data:
                beertype = item.get('beertype')
                beername = item.get('beername')
                beerbrewery = item.get('beerbrewery')
                beerNr = item.get('beerNr')
                beerCountry = item.get('beerCountry')
                beerAmount = item.get('beerAmount')
                beerPercentage = item.get('beerPercentage')
                beerPrice = item.get('beerPrice')

                beer = Beer(beertype=beertype,
                            beername=beername,
                            beerbrewery=beerbrewery,
                            beerNr=beerNr,
                            beerCountry=beerCountry,
                            beerAmount=beerAmount,
                            beerPercentage=beerPercentage,
                            beerPrice=beerPrice)
                beer.save()

        self.stdout.write(self.style.SUCCESS('Beer data loaded successfully'))