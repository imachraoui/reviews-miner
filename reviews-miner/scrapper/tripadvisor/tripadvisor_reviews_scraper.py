from bs4 import BeautifulSoup
import requests
import time as t
import re
import pandas as pd

reviews_df=pd.DataFrame()

searchlink= 'https://www.tripadvisor.fr/Restaurant_Review-g187147-d6575305-Reviews-Il_Etait_Un_Square-Paris_Ile_de_France.html'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
 
headers = {'User-Agent': user_agent}
 
links = [searchlink]

new_link = searchlink

while(True):

    try: 

        page = requests.get(new_link, headers = headers).text

        soup = BeautifulSoup(page, "lxml")

        link_next_page = soup.find("div",class_="listContainer hide-more-mobile").find("div", class_="unified ui_pagination").find("a", class_="nav next taLnk ui_button primary")["href"]

        new_link="https://www.tripadvisor.fr"+link_next_page

        links.append(new_link)

        # print(new_link)

        reviews_containers = soup.find_all("div",class_="review-container")

        for review_container in reviews_containers:
            
            review_container.find("div",class_="ui_column is-9")

            spans = review_container.find_all("span")
            rating = [r["class"] for r in spans if "ui_bubble_rating" in r["class"][0]][0][1][7]
            
            comment = review_container.find("div",class_="prw_rup prw_reviews_text_summary_hsx").text
 
            stay_date = review_container.find("div",class_="prw_rup prw_reviews_stay_date_hsx").contents[1].lstrip()
 
            print(stay_date)
 
            review_dict = {
                "review_rating" : rating,
                "review_date" : stay_date,
                "review_text" : comment
            }
 
            reviews_df = reviews_df.append(review_dict, ignore_index=True)
 
        reviews_df.to_csv("tripadvisor_reviews.csv", mode='a', header=False)

        t.sleep(2)

    except:

       break
 
print(links)
 
