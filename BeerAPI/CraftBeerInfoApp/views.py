import json
from django.http import HttpResponse, JsonResponse
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

# Create your views here.

# -------------------------------------------------------#
# the start page: no template
def home_view(request, *args, **kwargs):
    list_beers_url = reverse('beer-list')
    return HttpResponse(f"<div> <h1>Craft Beer list</h1> <br> <h2> Here below is a list of API options </h2> <a href='{list_beers_url}' target='_blank'>GET - List of all Craft Beers</a> </div>")

# the start page: with a template
def home_view(request, *args, **kwargs):

    # add all the beers to the view
    # add all the breweries to the view
    brewery_list = Brewery.objects.all().values()
    beer_list = Beer.objects.all().values()
    list_dict = {
        'brewery_list': brewery_list,
        'beer_list': beer_list
    }
    
    return render(request, 'home.html', list_dict)




# -------------------------------------------------------#
# 1: beers GET
class BeerListView(APIView):

    def get(self, request, format=None):
        beers = Beer.objects.all()
        if not beers:
            return Response({"detail": "No beers found."})
        serializer = BeerSerializer(beers, many=True)
        return Response(serializer.data)

    # POST
    # def post(self, request, format=None):
    #     serializer = BeerSerializer(data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------------------------------------------#
# 2: brewery GET
class BreweryListView(APIView):

    def get(self, request, format=None):
        brew= Brewery.objects.all()
        if not brew:
            return Response({"detail": "No breweries found."})
        serializer = BrewerySerializer(brew, many=True)
        return Response(serializer.data)

# -------------------------------------------------------#
# 1: beers POST
@api_view(['POST'])
def create_beer(request):
    beers_data = request.data
    serializer = BeerSerializer(data=beers_data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
Test object

{
"beertype" : "Öl, Ale, Amerikansk pale ale (APA)",
"beername"  : "Summer party",
"beerbrewery"   :  "Oceanbryggeriet",
"beerNr"  :  89509,
"beerCountry"  :  "Sweden",
"beerAmount"  :  "120ml",
"beerPercentage"   :  "5%",
"beerPrice"  :   "24:10"
}

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
    {"breweryName":"Sad Robot Brewing Co"},
    {"breweryName":"Beerbliotek"},
    {"breweryName":"Spike Brewery"},
    {"breweryName":"Vega Bryggeri"},
    {"breweryName":"Stigbergets Bryggeri"},
    {"breweryName":"Mohawk Brewing Company"},
    {"breweryName":"Billdale"},
    {"breweryName":"Beersmiths"},
    {"breweryName":"Duckpond Brewing"},
    {"breweryName":"Morgondagens Bryggeri"},
    {"breweryName":"Två Feta Grisar"},
    {"breweryName":"Bearded Rabbit Brewery"},
    {"breweryName":"All In Brewing"},
    {"breweryName":"Majornas Bryggeri"},
    {"breweryName":"Göteborgs Nya Bryggeri"}
]

"""

# -------------------------------------------------------#
# 1: PUT

class BeerUpdateView(UpdateAPIView):

    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

    def put(self, request, pk, *args, **kwargs):
        beer = self.get_object()
        serializer = self.serializer_class(beer, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------------------------------------------#
# 1: DELETE
class BeerDeleteView(generics.DestroyAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

    def perform_destroy(self, instance):
        if instance is None:
            raise ValidationError({'detail': 'Invalid beer ID provided.'})
        instance.delete()