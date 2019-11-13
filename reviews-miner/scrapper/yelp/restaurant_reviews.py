from bs4 import BeautifulSoup
import requests
import pandas as pd
 
reviews_df=pd.DataFrame()
 
searchlink= 'https://www.yelp.com/biz/the-purple-pig-chicago?osq=Restaurants'
 
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
 
headers = {'User-Agent': user_agent}
 
page = requests.get(searchlink, headers = headers).text
 
soup = BeautifulSoup(page, "lxml")
 
lists = soup.find("div",class_="lemon--div__373c0__1mboc pagination-links__373c0__2ZHo6 border-color--default__373c0__2oFDT nowrap__373c0__1_N1j")
 
 
 
print(lists.find_all("div", class_="lemon--div__373c0__1mboc pagination-link__373c0__1oL5g pagination-link--available__373c0__1UNRD display--inline-block__373c0__2de_K border-color--default__373c0__2oFDT")[-1].text)