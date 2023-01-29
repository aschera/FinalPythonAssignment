from django.db import models

# Create your models here.


# Entry some data into model
class beer(models.Model):
    Type = models.CharField(max_length=30, null=True)
    Name = models.CharField(max_length=10, null=True)
    Nr = models.CharField(max_length=10, null=True)
    Country = models.CharField(max_length=10, null=True)
    Amount = models.CharField(max_length=10, null=True)
    Percentage= models.CharField(max_length=10, null=True)
    Price = models.CharField(max_length=10, null=True)
    beer_quantity = models.CharField(max_length=10, null=True)
 
# Create a string representation
    def __str__(self):
        return self.Type # will return all the fields.