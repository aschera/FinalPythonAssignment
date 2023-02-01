from django.db import models

# Create your models here.


# Entry some data into model

class Beer(models.Model):

    # Fields
    Type = models.CharField(max_length=30, null=True)
    Name = models.CharField(max_length=10, null=True)
    Nr = models.CharField(max_length=10, null=True)
    Country = models.CharField(max_length=10, null=True)
    Amount = models.CharField(max_length=10, null=True)
    Percentage= models.CharField(max_length=10, null=True)
    Price = models.CharField(max_length=10, null=True)
    beer_quantity = models.CharField(max_length=10, null=True)
    
    # Meta data

    # Methods
    def __str__(self):
        return self.Name # will return name

    def list_data(self):
        return [self.Type, self.Name, self.Nr, self.Country, self.Amount, self.Percentage, self.Price, self.beer_quantity]



class GroupViewSet(models.Model):

    # Fields
    Type = models.CharField(max_length=30, null=True)
    Name = models.CharField(max_length=10, null=True)
 
    # Meta data

    # Methods
    def __str__(self):
        return self.Name # will return name

    def list_data(self):
        return [self.Type, self.Name]