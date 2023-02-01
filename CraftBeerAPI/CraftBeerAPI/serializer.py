# will take care of the SQL to JSON conversion


from rest_framework import serializers

from CraftBeerInfoApp.models import Beer, GroupViewSet



class BeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beer
        fields = ['Type', 
            'Name', 
            'Nr', 
            'Country',
            'Amount',
            'Percentage',
            'Price',
            'beer_quantity'
        ]
  
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupViewSet
        fields = ['Type', 'Name']