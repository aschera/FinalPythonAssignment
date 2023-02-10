# second table : Brewery
# ------------------------------------------------- #
create a second model and table by defining another class in your models.py file. For example, let's say you want to create a Brewery model, it might look like this:

class Brewery(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    founded_date = models.DateField()
    description = models.TextField()
You can then run python manage.py makemigrations and python manage.py migrate to create the new table in your database.

As for linking the two models, you can use a foreign key relationship. In the Beer model, you can add a foreign key to the Brewery model, like this:

class Beer(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    abv = models.FloatField()
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
To display the Brewery information along with the Beer information, you can create a serializer for the Brewery model, similar to the BeerSerializer, and include it as a nested serializer in the BeerSerializer.

Finally, you can create a view and URL pattern for the Brewery model, similar to what you did for the Beer model.

# pagination : 
# ------------------------------------------------- #

step-by-step guide to implementing PageNumberPagination in Django Rest Framework:

Install the library: If you haven't already, install the Django Rest Framework by running pip install djangorestframework.

Add it to your settings.py: Add 'rest_framework.pagination.PageNumberPagination' to your INSTALLED_APPS list in settings.py.

Define the pagination class: In your views.py, define the pagination class as follows:

from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5 # number of records per page
    page_size_query_param = 'page_size' # query parameter to control the page size
    max_page_size = 10 # maximum number of records returned per request
Apply the pagination class to your view: In your view, include the following code to apply the pagination class:


from rest_framework import generics

class BeerListView(generics.ListAPIView):
    pagination_class = CustomPageNumberPagination
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer


Test the pagination: 

Finally, make a request to your endpoint and observe the pagination in action. You can control the page size by passing the page_size query parameter in your request.
With these steps, you should have successfully implemented PageNumberPagination in your Django API app.



# ----------------------------------------------------- #
new scraper
https://medium.com/@kaismh/extracting-data-from-websites-using-scrapy-e1e1e357651a#.sw7c9ycio