from selenium import  webdriver
from time import sleep

url = 'http://www.google.com'

login_account = 'kenneth.chiao@gmail.com'
login_pwd = '19901211'

bw = webdriver.Safari()
bw.get(url)

bw.find_element_by_id('gb_70').click()

bw.find_element_by_id('identifierId').send_keys(login_account)
sleep(2)

bw.find_element_by_xpath("//span[@class='RevJvd snByac']").click()
sleep(2)

bw.find_element_by_xpath("//input[@type='password']").send_keys(login_pwd)
sleep(2)

bw.find_element_by_xpath("//span[@class='RevJvd snByac']").click()
sleep(3)

bw.quit()
