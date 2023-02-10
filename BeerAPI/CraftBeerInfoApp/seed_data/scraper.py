# https://www.systembolaget.se/sortiment/ol/sverige/vastra-gotalands-lan/goteborgs-stad/
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36

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

data= []

for a in soup.find_all('a'):

    newdict = []
    result = {}

    for p in a.find_all('div', class_ = 'css-1otywyl'):

        for r in p.find_all('p', class_ = 'css-4ijttz'): # the type: class css-4ijttz
            if r.text:
                beer = r.text.replace('\n',' ')
                beertype = re.sub('[\/]', ' ', beer)
                
        for s in p.find_all('p', class_ = 'css-w9tb7l'): # the name: class css-w9tb7l
            if s.text:
                beername = s.text.replace('\n',' ')

        for d in p.find_all('p', class_ = 'css-w9tb7l'): # the brewery: class css-w9tb7l
            if d.text:
                beerbrewery = d.text.replace('\n',' ')


        for t in p.find_all('p', class_ = 'css-10vqt1w'): # the nr: class css-10vqt1w 
            if t.text:
                only_numbers = re.compile(r'\d+(?:\.\d+)?') # pattern that only returns numbers
                beerNr = only_numbers.findall((t.text))
                beerNr = int(beerNr[0])
  
        # 3x : css-1e3a8ey (country, amount in ml, percentage alcohol)
        counter = 0
    
        keys = ['beerCountry', 'beerAmount', 'beerPercentage']
        for u in p.find_all('p', class_='css-1e3a8ey'):
            if u.text:
                result[keys[counter]] = u.text
                counter += 1
                if counter == 3:
                    continue

        for v in p.find_all('p', class_ = 'css-1kvpmze'): # the price: class css-1kvpmze
            if v.text:
                beerprice = v.text.replace('\n',' ')

        case = {'beertype': beertype, 'beerbrewery': beerbrewery,'beername': beername, 'beerNr': beerNr, 'beerprice': beerprice, 'beerCountry': result['beerCountry'], 'beerAmount': result['beerAmount'], 'beerPercentage': result['beerPercentage']}

        newdict.append(case)

        

    #test
    if newdict:
        data.append(newdict)

# initialize the file with an empty list:
# with open('beer_output1.json', mode='w', encoding='utf-8-sig') as f1:
#     json.dump([], f1)

#append new entries to this list:
# with open('beer_output1.json', mode='w', encoding='utf-8-sig') as f2:
#     json.dump(data, f2)  

# Create DataFrame
df1 = pd.DataFrame(data)

# make json from df
with open('beer_output2.json', 'w', encoding='utf-8', errors='ignore') as file:
    df1.to_json('beer_output2.json', force_ascii=False, orient='values')

# make csv file
# df1.to_csv("beer_output.csv", index=False, encoding='utf-8-sig' )

# make json file
#with open('df.json', 'w', encoding='utf-8', errors='ignore') as file:
#    df.to_json('beer_output.json', force_ascii=False)