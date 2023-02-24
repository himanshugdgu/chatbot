from lib2to3.pgen2 import driver
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
def timer_setter(user_query):
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\HIMANSHU SINGH\Downloads\Compressed\c_14\chromedriver.exe", options=chrome_options)
    url = "https://www.google.co.in/search?q=" + user_query
    driver.get(url)
    driver.minimize_window()

if __name__ == '__main__':
    print(timer_setter("set timer of 2 seconds"))
