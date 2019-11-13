from bs4 import BeautifulSoup
import requests
import pandas as pd
 
reviews_df=pd.DataFrame()
 
searchlink= 'https://www.yelp.com/biz/the-purple-pig-chicago?osq=Restaurants'
 
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
 
headers = {'User-Agent': user_agent}
 
page = requests.get(searchlink, headers = headers).text
soup = BeautifulSoup(page, "lxml")
 
 
lists = soup.find_all("li",class_="lemon--li__373c0__1r9wz u-space-b3 u-padding-b3 border--bottom__373c0__uPbXS border-color--default__373c0__2oFDT")
 
print(len(lists))
 
i=0
for list in lists :
 
    rating = list.find("div").contents[1].contents[0].contents[0].contents[0].span.div["aria-label"]
    date = list.find("div").contents[1].contents[0].contents[0].contents[1].span.text
    comment = list.find("div").contents[1].contents[2].text
    
    review_dict = {
        'rating' : rating,
        'date' : date,
        'comment' : comment
    }
 
    reviews_df = reviews_df.append(review_dict, ignore_index=True)
 
 
reviews_df.to_csv("reviews.csv")