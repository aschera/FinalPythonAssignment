"""BeerAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from CraftBeerInfoApp.views import BeerListView, BreweryListView, home_view, create_beer, create_beers, create_brewery, BeerUpdateView, BeerDeleteView   # <- import the views.


urlpatterns = [
    path('', home_view, name='home'), # the start page
    path('admin/', admin.site.urls), # the admin page

# -- BEER --    
    path("beer/", BeerListView.as_view(), name="beer-list"), # <- the beer list, GET request
    path('beer/create/', create_beer, name='create_beer'), # <- the create beer, POST request
    path('beer/create_many/', create_beers, name='create_beers'), # <- the create beer, POST request
    path('beer/<int:pk>/', BeerUpdateView.as_view(), name='update_beer'), # <- the update beer, PUT request
    path('beer/<int:pk>/delete/', BeerDeleteView.as_view(), name='delete_beer'),# <- the delete beer, DELETE request

    # -- BREWERY --
    path("brewery/", BreweryListView.as_view(), name="brewery-list"), # <- the brewery list, GET request
    path('brewery/create/', create_brewery, name='create_brewery'), # <- the create brewery, POST request

]
