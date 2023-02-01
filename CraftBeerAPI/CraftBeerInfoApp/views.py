from django.shortcuts import render

# Create your views here.
#-------------------------------------#

# import Http Response from django
from django.http import HttpResponse

from CraftBeerAPI.serializer import BeerSerializer, GroupSerializer

# create a function for HOME
def home(request):
    # convert to string
    html = " You can see all beer types under /beer. And all breweries under /brew. "
    # return response
    return HttpResponse(html)

#-------------------------------------#
# create a function for BEER

from django.template import loader
from .models import Beer

 
def beer(request):
    beer = Beer.objects.all().values()
    template = loader.get_template('all_beer.html')
    context = {
        'beer': beer,
    }
    return HttpResponse(template.render(context, request))

#-------------------------------------#


from django.contrib.auth.models import User, Group
from rest_framework import viewsets


class BeerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows beers to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = BeerSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer