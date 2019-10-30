from bs4 import BeautifulSoup
import requests

searchlink= 'https://www.yelp.com/biz/the-purple-pig-chicago?osq=Restaurants'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

headers = {'User-Agent': user_agent}

page = requests.get(searchlink, headers = headers).text
soup = BeautifulSoup(page, "lxml")


lists = soup.find_all("ul",class_="lemon--ul__373c0__1_cxs undefined list__373c0__2G8oH")

for list in lists :
    comments = list.find_all("span",class_="lemon--span__373c0__3997G")
    for comment in comments:
        print(comment.text)

---


from pytube import YouTube

print('Enter the video link: ',sep='/n')

link = input()

yt = YouTube(link)

yt.streams.first().download()