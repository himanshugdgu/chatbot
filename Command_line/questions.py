import requests
from bs4 import BeautifulSoup

list = ["vk_bk TylWce SGNhVe",  #weather
        "vk_bk dDoNo FzvWSb",  #date
        "gsrt vk_bk FzvWSb YwPhnf",  #time
        'IZ6rdc',
        'LGOjhe',
        "Z0LcW t2b5Cf CfV8xf",
        "vk_gy vk_sh card-section sL6Rbf",
        'Z0LcW t2b5Cf',
        'VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf',
        'yp1CPe wDYxhc NFQFxe viOShc LKPcQc',
        'vk_bk dDoNo FzvWSb',
        'X5LH0c',
        'IZ6rdc',
        'RqBzHd',
        'wob_t q8U8x',
        'LGOjhe',
        'LTKOO sY7ric'
        ]


def finder(user_query):
    try:
        URL = "https://www.google.co.in/search?q=" + user_query
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        result = None
        i = 0
        while (result == None and i < len(list)):
            result = soup.find('div', class_=list[i])
            i += 1
        return result.get_text()
    except Exception as e:
        print(e)
        return 'Sorry no result, please be clear'


if __name__ == '__main__':
    print(finder("who is cm of delhi"))
    # text = finder("what is a man")
    # print(list)
