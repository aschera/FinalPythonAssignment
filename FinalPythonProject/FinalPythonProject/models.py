from django.db import models

# Create your models here.


# Entry some data into model
class beer(models.Model):
    beer_name = models.CharField(max_length=10)
    company_name = models.CharField(max_length=10)
    beer_price = models.IntegerField()
    beer_quantity = models.IntegerField()
 
# Create a string representation
    def __str__(self):
        return self.beer_name # will return all the fields.