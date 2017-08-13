from selenium import  webdriver
from time import sleep
import  os
os.system('clear')

url = 'http://www.google.com'

login_account = '#######@gmail.com'
login_pwd = '######'

# chromedriver 的路徑
chrome_path = '/Users/kennethchiao/Desktop/PythonClass/Py_Paser/chromedriver'

# 開啟Chrome(driver_path)
bw = webdriver.Chrome(chrome_path)

# 開啟網址
bw.get(url)

# 找到Id為 gb_70 的物件 ， 點擊它
bw.find_element_by_id('gb_70').click()

# 找到Id為identifierId的物件 並賦予其帳號值()
bw.find_element_by_id('identifierId').send_keys(login_account)
sleep(2)

# 點擊繼續按鈕
bw.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
sleep(2)

# 輸入密碼
bw.find_element_by_xpath("//input[@type='password']").send_keys(login_pwd)
sleep(2)

# 點擊繼續
bw.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
sleep(3)

# 關閉瀏覽器
# bw.quit()
