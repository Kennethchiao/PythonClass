# coding=utf-8
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup as bs
import time

url ="https://www.agoda.com/zh-tw/pages/agoda/default/DestinationSearchResult.aspx?znrid=49002e95-ebf4-4991-941a-65f157ed23a8&city=4951&recommendedIndex=1&pageType=1&panel=searchboxrecommended&pagetypeid=1&origin=TW&cid=1732641&tag=41460a09-3e65-d173-1233-629e2428d88e&gclid=CjwKCAjw_dTMBRBHEiwApIzn_Ilrojz3eBQV23h0AlCOinuPXoZc53tXGOPGz6e45OzCKhTxsyMh5xoC_FIQAvD_BwE&aid=81837&userId=e825b2a8-7175-4ab1-8a10-25cb01492beb&languageId=20&sessionId=q4dtjg1w4eoh1c0ous3brmei&storefrontId=3&currencyCode=TWD&htmlLanguage=zh-tw&trafficType=User&cultureInfoName=zh-TW&checkIn=2017-08-27&checkOut=2017-08-28&los=1&rooms=1&adults=2&children=0&childages=&priceCur=TWD&hotelReviewScore=5&ckuid=e825b2a8-7175-4ab1-8a10-25cb01492beb"

browser = webdriver.Chrome("/Users/kennethchiao/Desktop/PythonClass/Py_Paser/chromedriver")
browser.get(url)
# try:
browser.find_element_by_xpath('//button[contains(@class="btn btn-right")]')
# except Exception as e:
#     print('ERROR')

# browser.close()
