# https://www.systembolaget.se/sortiment/ol/sverige/vastra-gotalands-lan/goteborgs-stad/
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36

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


with open('assets/beer_website_source.html', encoding='utf-8-sig') as f:  
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
#        "fields": 
#    }
# ]

    p_tags = []

    for a in soup.find_all('a'):
        a_data = []

        for p in a.find_all('div', class_ = 'css-1otywyl'):

            for r in p.find_all('p', class_ = 'css-4ijttz'): # the type: class css-4ijttz
                if r.text:
                    text1 = r.text.replace('\n',' ')
                    a_data.append(text1)
                else:
                    a_data.append(' ')
            
            for s in p.find_all('p', class_ = 'css-w9tb7l'): # the name: class css-w9tb7l
                if s.text:
                    text2 = s.text.replace('\n',' ')
                    a_data.append(text2)
                else:
                    a_data.append(' ')

            for t in p.find_all('p', class_ = 'css-10vqt1w'): # the nr: class css-10vqt1w 
                if t.text:
                    text3 = t.text.replace('\n',' ')
                    a_data.append(text3)
                else:
                    a_data.append(' ')
            
            for u in p.find_all('p', class_ = 'css-1e3a8ey'): # 3x : css-1e3a8ey (country, amount in ml, percentage alcohol)
                if u.text:
                    text4 = u.text.replace('\n',' ')
                    a_data.append(text4)
                else:
                    a_data.append(' ')

            for v in p.find_all('p', class_ = 'css-1kvpmze'): # the price: class css-1kvpmze
                if v.text:
                    text5 = v.text.replace('\n',' ')
                    a_data.append(text5)
                else:
                    a_data.append(' ')

        if a_data:
            p_tags.append(a_data)

    # make dat frame
    df = pd.DataFrame(p_tags)
    df.columns=['Type', 'Name', 'Nr', 'Country', 'Amount', 'Percentage', 'Price']

    # make csv file
    # df.to_csv("assets/beer_output.csv", index=False, encoding='utf-8-sig' )

    import json
    # make json file
    with open('df.json', 'w', encoding='utf-8', errors='ignore') as file:
        df.to_json('assets/beer_output.json', force_ascii=False)