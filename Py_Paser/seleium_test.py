# https://chromedriver.storage.googleapis.com/index.html?path=2.31/
# 從selenium 使用 webdriver
from selenium import webdriver

# 選擇需自動化操作瀏覽器-需要另外安裝driver

broswer = webdriver.Chrome("/Users/kennethchiao/Desktop/PythonClass/Py_Paser/chromedriver")
# bw = webdriver.Safari()

# 利用browser開啟網址
# bw.get('http://www.google.com')
broswer.get('https://github.com/Kennethchiao/PythonClass')
# 關閉 browser
# bw.quit()
