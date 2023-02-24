
import requests
from bs4 import BeautifulSoup

def comparision(query):
    url = "https://www.flipkart.com/search?q="+query
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    diff = soup.find("div", class_="head")
    print(diff)
    return ("a")

comparision("macbook 1")

# price comparision between macbook 1 and macbook 2