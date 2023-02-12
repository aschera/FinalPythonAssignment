# https://www.systembolaget.se/sortiment/ol/sverige/vastra-gotalands-lan/goteborgs-stad/
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36

# brewery list: https://www.goteborg.com/en/guides/craft-beer-and-breweries-in-gothenburg

from collections import defaultdict
from bs4 import BeautifulSoup
import requests

# for URL
# with requests.Session() as se:
#     se.headers = {
 #        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
 #        "Accept-Encoding": "gzip, deflate",
  #       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
   #      "Accept-Language": "en"
   #  }


# site = 'https://www.systembolaget.se/sortiment/ol/sverige/vastra-gotalands-lan/goteborgs-stad/'
# response = se.get(site)
# print(response)
# print(response.text)

# soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

# ------------------------------------------------------------------ #

# for file


with open('beer_website_source.html', encoding='utf-8-sig') as f:  
    #read File
    content = f.read()
    #parse HTML
    soup = BeautifulSoup(content, 'html.parser')


    import pandas as pd


# fixture format:
# [
#    {
#        "pk": "1",
#        "model": "store.Beer",
#        "fields": {}
#    }
# ]

import re  # regular expressions, to find the data - exclude letters and spaces.
from typing import List
import json

# reset values
data= []

for a in soup.find_all('a'):

    # reset values
    newdict = []
    result = {}

    for p in a.find_all('div', class_ = 'css-1otywyl'):


        #----------------------- T Y P E ------------------------------------------# 
        beerType = ''
        for r in p.find_all('p', class_ = 'css-4ijttz'): # the type: class css-4ijttz
            if r.text:
                beer = r.text.replace('\n',' ')
                beerType = re.sub('[\/]', ' ', beer)


        #----------------------- N A M E ------------------------------------------#  
        beerName = ''
        for d in p.find_all('p', class_ = 'css-9c24zl'): # the brewery: class css-9c24zl
            if d.text:
                beerName = d.text.replace('\n',' ')


        #----------------------- B R E W E R Y ------------------------------------------#
        beerBrewery = ''           
        for s in p.find_all('p', class_ = 'css-w9tb7l'): # the name: class css-w9tb7l
            if s.text:
                beerBrewery = s.text.replace('\n',' ')

                #----------- O/O ------------#
                if s.text.startswith('O/O'):
                    beerBrewery =  'O/O Brewing'
                if s.text.startswith('O/O Pivot Pils'):
                    beerName= "Pivot Pils"
                if s.text.startswith('O/O Porter Porter'):
                    beerName= "Porter Porter"
                if s.text.startswith('O/O Pretty Pale Ale'):
                    beerName= "Pretty Pale Ale"
                if s.text.startswith('O/O A.B.W American Barley Wine'):
                    beerName= "A.B.W American Barley Wine"
                if s.text.startswith('O/O Festbier'):
                    beerName= "Festbier"
                    
                #----------- All In Brewing------------#
                if s.text.startswith(''):
                    beerBrewery =  'All In Brewing'
                    beerName= "8th year Stout"
  
                #----------- Beerbliotek ------------#
                if s.text.startswith('Beerbliotek'):
                    beerBrewery =  'Beerbliotek'

                #----------- Beersmiths ------------#    
                if s.text.startswith('Barley Wine'):
                    beerBrewery =  'Beersmiths'
                    beerName= "Barley Wine"
                if s.text.startswith('Retard Beer'):
                    beerBrewery =  'Beersmiths'
                    beerName= "Retard Beer"
                    
                #----------- Bearded Rabbit Brewery ------------#    
                if s.text.startswith('Åttonde Mars'):
                    beerBrewery =  'Bearded Rabbit Brewery'
                    beerName= "Åttonde Mars"
                if s.text.startswith('Bearded Rabbit'):
                    beerBrewery =  'Bearded Rabbit Brewery'
                if s.text.startswith('Monkish'):
                    beerBrewery =  'Bearded Rabbit Brewery'
                    beerName= "Monkish"
                if s.text.startswith('Floda Pilsner'):
                    beerBrewery =  'Bearded Rabbit Brewery'
                    beerName= "Floda Pilsner"
                if s.text.startswith('Bunny Blood'):
                    beerBrewery =  'Bearded Rabbit Brewery'
                    beerName= "Bunny Blood"
                if s.text.startswith('Doppelgänger'):
                    beerBrewery =  'Bearded Rabbit Brewery'
                    beerName= "Doppelgänger"

                #----------- Billdale ------------#
                if s.text.startswith('Billdale'):
                    beerBrewery =  'Billdale'
                if s.text.startswith('Billdale Caribbean Sun'):
                    beerName= "Caribbean Sun"
                if s.text.startswith('Diamante'):
                    beerBrewery =  'Billdale'
                    beerName= "Diamante"
                if s.text.startswith('True Love'):
                    beerBrewery =  'Billdale'
                    beerName= "True Love"
                    

                #----------- Sad Robot Brewing Co ------------#
                if s.text.startswith('Sad Robot'):
                    beerBrewery =  'Sad Robot Brewing Co'
                if s.text.startswith('Eightysix'):
                    beerBrewery =  'Sad Robot Brewing Co'
                    beerName= "Eightysix"
                   

                #----------- Spike Brewery ------------#
                if s.text.startswith('Burger Beer'):
                    beerBrewery =  'Spike Brewery'
                    beerName= "Burger Beer"
                if s.text.startswith('Flowers'):
                    beerBrewery =  'Spike Brewery'
                    beerName= "Flowers"
                    
                #----------- Duckpond Brewing ------------#
                if s.text.startswith('DuckPond'):
                    beerBrewery =  'Duckpond Brewing'
                if s.text.startswith('Duckpond'):
                    beerBrewery =  'Duckpond Brewing'
    
                #----------- Mohawk ------------#
                if s.text.startswith('Mohawk'):
                    beerBrewery =  'Mohawk Brewing Company'
                if s.text.startswith('Mohawk Doubleishious'):
                    beerName= "Doubleishious"
                if s.text.startswith('Mohawk Bärså'):
                    beerName= "Bärså"
                
                #----------- Två Feta Grisar ------------#
                if s.text.startswith('Två Feta Grisar'):
                    beerBrewery =  'Två Feta Grisar'
                if s.text.startswith('Dubbel 2.0'):
                    beerBrewery =  'Två Feta Grisar'
                    beerName= "Dubbel 2.0" 
                if s.text.startswith('Optimus'):
                    beerBrewery =  'Två Feta Grisar'
                if s.text.startswith('Coma'):
                    beerBrewery =  'Två Feta Grisar'
                    beerName= "Coma" 
                if s.text.startswith('Ring Öl'):
                    beerBrewery =  'Två Feta Grisar'
                    beerName= "Ring Öl" 
                if s.text.startswith('Mörk Vienna'):
                    beerBrewery =  'Två Feta Grisar'
                    beerName= "Mörk Vienna" 
                if s.text.startswith('Diamant'):
                    beerBrewery =  'Två Feta Grisar'
                    beerName= "Diamant" 


                #----------- Stigbergets ------------#
                if s.text.startswith('Stigbergets'):
                    beerBrewery =  'Stigbergets Bryggeri'
                if s.text.startswith('Stigbergets ÖL'):
                    beerName= "ÖL"
                if s.text.startswith('Stigbergets Trouble Sleep'):
                    beerName= "Trouble Sleep" 
                if s.text.startswith('Stigbergets DH-DDH-WC IPA'):
                    beerName= "Double Headed DDH West Coast IPA" 
                if s.text.startswith('Stigbergets American Pale Ale'):
                    beerName= "American Pale Ale" 
                if s.text.startswith('Stigbergets Session IPA'):
                    beerName= "Session IPA" 
                    

                #----------- Spike Brewery ------------#
                if s.text.startswith('Spike'):
                    beerBrewery =  'Spike Brewery'
                if s.text.startswith('Aciid'):
                    beerBrewery =  'Spike Brewery'
                    beerName= "Aciid" 
                if s.text == 'Spike':
                    beerBrewery =  'Spike Brewery'
                    beerName= "Spike" 
                if s.text == 'Fingerlickin':
                    beerBrewery =  'Spike Brewery'
                    beerName= "Fingerlickin'" 
                    
                    
                #----------- Göteborgs Nya Bryggeri ------------#
                if s.text.startswith('Gothenburg brew'):
                    beerBrewery =  'Göteborgs Nya Bryggeri'
                if s.text.startswith('Gothenburg Brew'):
                    beerBrewery =  'Göteborgs Nya Bryggeri'
                if s.text.startswith('Gothenburg brew West Coast Fog'):
                    beerName= "West Coast Fog"
                if s.text.startswith('Göteborgs Winter Ale'):
                    beerName= "Winter Ale"
                if s.text.startswith('Chuck the Oyster'):
                    beerName= "Chuck the Oyster"
                    beerBrewery =  'Göteborgs Nya Bryggeri'
                if s.text.startswith('Göteborgs Sommar Lager'):
                    beerName= "Sommar Lager"  
                if s.text.startswith('Göteborgs Summer Pale Ale  '):
                    beerName= "Summer Pale Ale  "  
                if s.text.startswith('Göteborgs Stora Starkpilsner'):
                    beerName= "Göteborgs Stora Starkpilsner"
                if s.text.startswith('Göteborgs Jul-Öl'):
                    beerName= "Jul-Öl"
                if s.text.startswith('Göteborgs'):
                    beerBrewery =  'Göteborgs Nya Bryggeri'
                if s.text.startswith('1810 Oktoberfestöl'):
                    beerBrewery =  'Göteborgs Nya Bryggeri'
                    beerName= "1810 Oktoberfestöl"

                #----------- Majornas Bryggeri ------------#
                if s.text.startswith('Majornas'):
                    beerBrewery =  'Majornas Bryggeri'
                if s.text.startswith('Elfsborgs Lösen'):
                    beerBrewery =  'Majornas Bryggeri'
                    beerName= "Elfsborgs Lösen"
                if s.text.startswith('Majornas Kaparkung'):
                    beerBrewery =  'Majornas Bryggeri'
                    beerName= "Kaparkung"
                if s.text.startswith('Majornas Citra'):
                    beerBrewery =  'Majornas Bryggeri'
                    beerName= "Majornas Citra"    
                if s.text.startswith('Knô daj in'):
                    beerBrewery =  'Majornas Bryggeri'
                    beerName= "Knô daj in" 
                if s.text.startswith('Majornas EPA'):
                    beerBrewery =  'Majornas Bryggeri'
                    beerName= "Majornas EPA" 
                if s.text.startswith('Älska'):
                    beerBrewery =  'Majornas Bryggeri'
                    beerName= "Älska"
                if s.text.startswith('Majornas Höstale'):
                    beerBrewery =  'Majornas Bryggeri'
                    beerName= "Majornas Höstale "
                       

                #----------- Morgondagens Bryggeri------------#
                if s.text.startswith('Morgondagens'):
                    beerBrewery =  'Morgondagens Bryggeri'
                if("Deadhead" in s.text):
                    beerName= "Deadhead"
                if s.text.startswith('Morgondagens Misshappen'):
                    beerName= "Misshappen"
                    beerBrewery =  'Morgondagens Bryggeri'
                    
                #----------- Vega Bryggeri ------------#
                if s.text.startswith('Winter Island Stout'):
                    beerBrewery =  'Vega Bryggeri'
                    beerName= "Winter Island Stout"
                if s.text.startswith('Winter Island Ale'):
                    beerBrewery =  'Vega Bryggeri'
                    beerName= "Winter Island Ale"
                if s.text.startswith('Vega Easter Lager'):
                    beerName= "Vega Easter Lager"
                if s.text.startswith('The Holy Grail'):
                    beerBrewery =  'Vega Bryggeri'
                    beerName= "The Holy Grail"
                if s.text.startswith('Vega'):
                    beerBrewery =  'Vega Bryggeri'
                if s.text.startswith('Double Dry Hopped IPA'):
                    beerBrewery =  'Vega Bryggeri'
                    beerName= "Double Dry Hopped IPA"


                    
                    
        #----------------------- N R ------------------------------------------#
        beerNr = 0 
        for t in p.find_all('p', class_ = 'css-10vqt1w'): # the nr: class css-10vqt1w 
            if t.text:
                only_numbers = re.compile(r'\d+(?:\.\d+)?') # pattern that only returns numbers
                beerNr = only_numbers.findall((t.text))
                beerNr = int(beerNr[0])
  

        #----------------------- 'beerCountry', 'beerAmount', 'beerPercentage' ------------------------------------------#
        # 3x : css-1e3a8ey (country, amount in ml, percentage alcohol)
        counter = 0
    
        keys = ['beerCountry', 'beerAmount', 'beerPercentage']
        for u in p.find_all('p', class_='css-1e3a8ey'):
            if u.text:
                result[keys[counter]] = u.text
                counter += 1
                if counter == 3:
                    continue

        #----------------------- P R I C E ------------------------------------------#
        beerPrice = 0.0
        for v in p.find_all('p', class_ = 'css-1kvpmze'): # the price: class css-1kvpmze
            if v.text:
                beerPrice = v.text.replace(':', '.').replace('*', '').replace('-', '0')

                beerPrice = float(str(beerPrice))  # because of the model type: beerPrice = models.DecimalField(max_length=10, null=True, decimal_places=2, max_digits=10000)

        
        case = {'beerType': beerType, 'beerName': beerName, 'beerBrewery': beerBrewery,   'beerNr': beerNr, 'beerPrice': beerPrice, 'beerCountry': result['beerCountry'], 'beerAmount': result['beerAmount'], 'beerPercentage': result['beerPercentage']}


        newdict.append(case)

        
    #test
    if newdict:
        data.append(newdict)



# ------------------------Add brewry list -----------------------------------#
breweries = set()
for beer in data:
    brewery = beer[0]["beerBrewery"]
    breweries.add(brewery)


unique_breweries = list(breweries)

# Writing the list to a JSON file
with open('breweries_output.json', 'w', encoding='utf-8', errors='ignore') as file:
    json.dump(unique_breweries, file, ensure_ascii=False)

# ------------------------make fixture -----------------------------------#

''' 
has to look like this
[
    {
        "model": "CraftBeerInfoApp.beer",
        "pk": 1,
        "fields": {}
        }
]
'''

fixture = {
    "model": "CraftBeerInfoApp.beer",
    "pk": 1,
    "fields": { "data": data }
}

with open('breweries_output_fixture.json', 'w', encoding='utf-8', errors='ignore') as file:
    json.dump(fixture, file, ensure_ascii=False)

# python manage.py loaddata CraftBeerInfoApp/seed_data/beer_output_fixture.json
 


# ------------------------Add beer list -----------------------------------#

# initialize the file with an empty list:
# with open('beer_output1.json', mode='w', encoding='utf-8-sig') as f1:
#     json.dump([], f1)

#append new entries to this list:
# with open('beer_output1.json', mode='w', encoding='utf-8-sig') as f2:
#     json.dump(data, f2)  

# make json from df
# Writing the list to a JSON file
# with open('beer_output.json', 'w', encoding='utf-8', errors='ignore') as file:
#    json.dump(data, file, ensure_ascii=False)


# Create DataFrame
#df2 = pd.DataFrame(data)

# make csv file
# df1.to_csv("beer_output.csv", index=False, encoding='utf-8-sig' )

# make json file
#with open('df.json', 'w', encoding='utf-8', errors='ignore') as file:
#    df.to_json('beer_output.json', force_ascii=False)