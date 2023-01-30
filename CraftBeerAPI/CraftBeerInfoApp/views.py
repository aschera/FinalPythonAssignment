from django.shortcuts import render

# Create your views here.
#-------------------------------------#

# import Http Response from django
from django.http import HttpResponse

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