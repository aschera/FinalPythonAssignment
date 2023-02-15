from django.db import models

# Create your models here.
class Brewery(models.Model):
    breweryName = models.CharField(max_length=100, unique=True)

class Beer(models.Model):

    # fields
    beerType= models.CharField(max_length=100)
    beerName = models.CharField(max_length=100)
    beerBrewery = models.ForeignKey(Brewery, on_delete=models.CASCADE, related_name='beers')
    beerNr = models.IntegerField()
    beerCountry = models.CharField(max_length=10, null=True)
    beerAmount = models.CharField(max_length=10, null=True)
    beerPercentage= models.CharField(max_length=10, null=True)
    beerPrice = models.DecimalField(max_length=10, null=True, decimal_places=2, max_digits=10000)

    def __str__(self):
        return self.beerName


