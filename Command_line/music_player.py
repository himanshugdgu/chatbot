from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument = {
#     'user-data-dir': '/Users/Application/Chrome/Default'}
# chrome_options.add_argument(r"C:\Users\HIMANSHU SINGH\AppData\Local\Google\Chrome\User Data\Default")

def music_url_opener(query):
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\HIMANSHU SINGH\Downloads\Compressed\c_14\chromedriver.exe", options=chrome_options)
    url = "https://www.youtube.com/results?search_query="+query
    driver.get(url)
    driver.find_element("xpath", '//*[@id="video-title"]').click()
    driver.find_element("xpath", '//*[@id="button"]').click()


    # print("*************** "+type(video))
    # video.click()
    # driver.minimize_window()
# music_url_opener("apni to jaise tese song")
