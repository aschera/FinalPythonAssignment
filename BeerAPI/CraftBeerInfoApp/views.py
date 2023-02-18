from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
 
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from rest_framework.exceptions import ValidationError

from .models import Beer, Brewery # <- import the model.
from .serializers import BeerSerializer, BrewerySerializer # <- import the serializer

# -------------------------------------------------------#
# the start page: no template

def home_view(request, *args, **kwargs):
    list_beers_url = reverse('beer-list')
    return HttpResponse(f"<div> <h1>Craft Beer list</h1> <br> <h2> Here below is a list of API options </h2> <a href='{list_beers_url}' target='_blank'>GET - List of all Craft Beers</a> </div>")

# the start page: with a template

def home_view(request, *args, **kwargs):
    # Retrieve all the Brewery and Beer objects from the database
    brewery_list = Brewery.objects.all().values()
    beer_list = Beer.objects.all().values()
    # Store the Brewery and Beer objects in a dictionary for use in the template
    list_dict = {
        'brewery_list': brewery_list,
        'beer_list': beer_list
    }
    
    # Render the home.html template with the list_dict data
    return render(request, 'home.html', list_dict)


# -------------------------------------------------------#
# 1: beers GET

class BeerListView(APIView):

    def get(self, request, format=None):
        # Retrieve all the Beer objects from the database
        beers = Beer.objects.all()
        # Check if any Beer objects were found
        if not beers:
            # If no Beer objects were found, return a 404 error with a descriptive message
            return Response({"detail": "No beers found."})
        # If Beer objects were found, serialize them and return the data
        serializer = BeerSerializer(beers, many=True)
        return Response(serializer.data)

# -------------------------------------------------------#
# 2: brewery GET

class BreweryListView(APIView):

    def get(self, request, format=None):
        # Retrieve all the Brewery objects from the database
        brew= Brewery.objects.all()
        # Check if any Brewery objects were found
        if not brew:
            # If no Brewery objects were found, return a 404 error with a descriptive message
            return Response({"detail": "No breweries found."})
        # If Brewery objects were found, serialize them and return the data
        serializer = BrewerySerializer(brew, many=True)
        return Response(serializer.data)

# -------------------------------------------------------#
# 1: beers POST

@api_view(['POST'])
def create_beer(request):
    # Extract the beer data from the request
    beers_data = request.data
    # Use the BeerSerializer to validate and serialize the data
    serializer = BeerSerializer(data=beers_data, many=True)
    # Check if the serializer is valid
    if serializer.is_valid():
        # Save the new Beer objects to the database
        serializer.save()
        # Return the serialized data with a 201 status code
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # If the serializer is not valid, return the errors with a 400 status code
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
Test object

[
    {
    "beertype" : "Öl",
    "beername"  : "Tarty",
    "beerbrewery"   :  "Bryggeriet",
    "beerNr"  :  12345,
    "beerCountry"  :  "Sweden",
    "beerAmount"  :  "100ml",
    "beerPercentage"   :  "15%",
    "beerPrice"  :   "25:10"
    }
]

"""

# -------------------------------------------------------#
# 2: POST

@api_view(['POST'])
def create_brewery(request):
    brewery_data = request.data
    serializer = BrewerySerializer(data=brewery_data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
Test object

[
    {
        "id": 100,
        "breweryName": "Brewing Co 100"
    }
]


"""

# -------------------------------------------------------#
# 1: PUT

class BeerUpdateView(UpdateAPIView):

    # Set queryset to get all the Beer objects from the database
    queryset = Beer.objects.all()
    
    # Use the BeerSerializer to validate and serialize the data
    serializer_class = BeerSerializer

    def put(self, request, pk, *args, **kwargs):
        # Retrieve the specific Beer object we want to update
        beer = self.get_object()
        # Use the serializer to validate and update the Beer object
        serializer = self.serializer_class(beer, data=request.data)

        # If the serializer is valid, save the updated Beer object and return the updated data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # If the serializer is not valid, return the errors with a 400 status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------------------------------------------#
# 1: DELETE

class BeerDeleteView(generics.DestroyAPIView):

    # Set queryset to get all the Beer objects from the database
    queryset = Beer.objects.all()

    # Use the BeerSerializer to validate and serialize the data
    serializer_class = BeerSerializer

    def perform_destroy(self, instance):
        # Check if the Beer object we want to delete exists
        if instance is None:
            # If it doesn't exist, raise a validation error with a descriptive message
            raise ValidationError({'detail': 'Invalid beer ID provided.'})
        
        # If the Beer object exists, delete it
        instance.delete()
