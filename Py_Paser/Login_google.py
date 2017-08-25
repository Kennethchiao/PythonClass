from selenium import  webdriver
from time import sleep

url = 'http://www.google.com'

login_account = 'kthon.co@gmail.com'
login_pwd = 'pythonclass'

bw = webdriver.Chrome("/Users/kennethchiao/Desktop/PythonClass/Py_Paser/chromedriver")
# bw = webdriver.Safari()
bw.get(url)

bw.find_element_by_id('gb_70').click()

bw.find_element_by_id('identifierId').send_keys(login_account)
sleep(2)

bw.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
sleep(2)

bw.find_element_by_xpath("//input[@type='password']").send_keys(login_pwd)
sleep(2)

bw.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
sleep(3)

# bw.quit()
