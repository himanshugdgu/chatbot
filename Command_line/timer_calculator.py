import requests
from bs4 import BeautifulSoup

def get_timer(user_query):
    try:
        URL = "https://www.google.co.in/search?q=" + user_query
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        result = None
        result = soup.find('div', class_="act-tim-txt-cnt q8U8x")
        
        return result.get_text()
    except Exception as e:
        print(e)
        return 'Please connect to internet'


if __name__ == '__main__':
    print(get_timer("set timer for 5 sec"))
    # text = finder("what is a man")
    # print(list)
