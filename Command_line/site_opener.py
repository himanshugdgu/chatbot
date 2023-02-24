from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    executable_path=r"C:\Users\HIMANSHU SINGH\Downloads\Compressed\c_14\chromedriver.exe", options=chrome_options)

driver.get("https://poki.com/en/g/subway-surfers")
