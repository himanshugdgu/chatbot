import requests
from bs4 import BeautifulSoup

def extract():
    url = 'https://www.news18.com/'
    news = []
    r=requests.get(url)
    soup = BeautifulSoup (r.text,'html.parser')
    divclass = soup.find_all('h2',class_="jsx-422283147 right_heading")
    for i in divclass:
        news.append(i.text)
    return news

if __name__ == "__main__":
    news = extract()
    print(news)
