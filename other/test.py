import requests
from bs4 import BeautifulSoup

response=requests.get(url="https://kun.uz/uz") 
# print(response.content)
soup=BeautifulSoup(response.content,"lxml")
title=soup.find("span",class_="big-news__title").get_text()
body=soup.find("span",class_="big-news__description").get_text()
a=soup.find_all("a",class_="news-lenta")
print(title)
print(body)