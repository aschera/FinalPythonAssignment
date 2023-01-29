from django.shortcuts import render

# Create your views here.
#-------------------------------------#

# import Http Response from django
from django.http import HttpResponse
# get datetime
import datetime
 
# create a function for HOME
def home(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)

#-------------------------------------#
# create a function for BEER

# relative import 
from .models import beer
 
def beer(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = beer.objects.all()
         
    return render(request, "list_view.html", context)