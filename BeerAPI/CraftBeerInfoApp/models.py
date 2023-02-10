from django.db import models

# Create your models here.
class Beer(models.Model):

    # fields
    beertype= models.CharField(max_length=100)
    beername = models.CharField(max_length=100)
    beerbrewery = models.CharField(max_length=100)
    beerNr = models.IntegerField()
    beerCountry = models.CharField(max_length=10, null=True)
    beerAmount = models.CharField(max_length=10, null=True)
    beerPercentage= models.CharField(max_length=10, null=True)
    beerPrice = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name