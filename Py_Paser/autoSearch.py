import  selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

web = webdriver.Chrome("/Users/kennethchiao/Desktop/PythonClass/Py_Paser/chromedriver")

web.get('http://www.google.com')

elem = web.find_element_by_name('q')
elem.send_keys('焦小龍')
elem.submit()

# web.quit()
