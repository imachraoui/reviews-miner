import pandas as pd
import time as t
from lxml import html
import requests

reviews_df=pd.DataFrame()

searchlink= 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Chicago,+IL'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

headers = {'User-Agent': user_agent}

page = requests.get(searchlink, headers = headers)

parser = html.fromstring(page.content)

businesslink=parser.xpath('//*[@id="wrap"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/ul/li/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/p/a')

print(len(businesslink))

links = [l.get('href') for l in businesslink]

u=[]

for link in links:
    if "?osq=Restaurants" in link:
        print(link, sep = "\n")
        u.append('https://www.yelp.com'+ str(link))
