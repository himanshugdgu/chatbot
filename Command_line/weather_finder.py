import requests
from bs4 import BeautifulSoup

list = ["vk_bk TylWce SGNhVe","wtsRwe"]


def weather_forecast():
    try:
        URL = "https://www.google.co.in/search?q=" + "weather in gurgaon"
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        temp = soup.find('div', class_=list[0]).get_text()
        temp = ''.join(temp.split())
        temp = temp[:-2]+" °C"
        other_details = soup.find('div', class_=list[1]).get_text()
        other_details=other_details.split("%")
        other_details[0]=other_details[0]+"%"
        other_details[1]=other_details[1]+"%"
        other_details[2] = other_details[2].split('h')[0]+'h'
        other_details.insert(0,temp)
        return other_details
    except Exception as e:
        print(e)
        return 'please make sure you are connected to internet'


if __name__ == '__main__':
    print(weather_forecast())
    # text = finder("what is a man")
    # print(list)
