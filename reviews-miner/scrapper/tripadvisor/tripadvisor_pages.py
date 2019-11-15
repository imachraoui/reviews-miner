from bs4 import BeautifulSoup
import requests
import time as t
import re
import pandas as pd
 

def getNextPageLinks(searchlink, user_agent, headers):

    links = [searchlink]
    
    new_link = searchlink

    while(True):
    
        try: 
    
            page = requests.get(new_link, headers = headers).text

            soup = BeautifulSoup(page, "lxml")
    
            link_next_page = soup.find("div",class_="listContainer hide-more-mobile").find("div", class_="unified ui_pagination").find("a", class_="nav next taLnk ui_button primary")["href"]
    
            new_link="https://www.tripadvisor.fr"+link_next_page
    
            links.append(new_link)
    
            print(new_link)
    
        except:
            break
    
    return links
  

 
searchlink= 'https://www.tripadvisor.fr//Restaurant_Review-g187147-d10514254-Reviews-or1030-Les_Apotres_de_Pigalle-Paris_Ile_de_France.html'
 
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
 
headers = {'User-Agent': user_agent}
 
print(getNextPageLinks(searchlink, user_agent, headers))
