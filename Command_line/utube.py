from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r"C:\Users\HIMANSHU SINGH\Downloads\Compressed\c_14\chromedriver.exe",options=options)
driver.maximize_window()
driver.get("http://youtube.com/")
sb = driver.find_element('xpath','//*[@id="search"]')
sb.send_keys('dsa')
tb = driver.find_element('xpath','//*[@id="search-icon-legacy"]')
tb.click()





















# from selenium import webdriver

# driver = webdriver.Chrome(executable_path=r"C:\Users\HIMANSHU SINGH\Downloads\Compressed\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://www.geeksforgeeks.org/15-must-have-javascript-tools-for-developers/")
# sb = driver.find_element('xpath','//*[@id="gcse-form"]/button')
# sb.click()
# tb = driver.find_element('xpath','//*[@id="gcse-search-input"]')
# tb.send_keys('dsa')
# tb.submit()
# # sb.send_keys("hitesh chaudhary")
