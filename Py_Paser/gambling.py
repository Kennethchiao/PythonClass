# 台灣彩卷威力彩開獎結果

import requests as rqs ,os
from bs4 import BeautifulSoup as BS

os.system("clear")
# 定義網址
url = 'http://www.taiwanlottery.com.tw/'
# 利用requests抓取此網頁資料
html = rqs.get(url)
# 利用 BeautifulSoup 解析網頁資料
soup = BS(html.text,'html.parser')
# 抓出網頁屬性 ID = rightdown 的 <div> 並回傳串列至 data1
data1 = soup.select("#rightdown")
# print(data1)
# 從串列中找出 class = 'contents_box02'的< div>
data2 = data1[0].find('div',{'class':'contents_box02'})
# print(data2)
# 再次重 data2 抓出 class = "ball_tx" 的 <div>
data3 = data2.find_all('div',{'class':'ball_tx'})
# print(data3)

# 實作區塊
# ==============================
# 期號  class tag = font_black15
#      屬性為 <span>
# ==============================

# Numbers =
print(' 樂透彩最新一期開獎號碼')
print(" 開出Order: ",end="")
for n in range(0,6):
    print(data3[n].text,end="  ")

print("\n 開出Order: ",end="")
for n in range(6,len(data3)):
    print(data3[n].text,end="  ")

#區號
second = data2.find('div',{'class':'ball_red'})
print("\n 第二區: {}".format(second.text))
print()
# 實作時間：把最新一期改成樂透彩開獎期號












# data4 = data2.find_all('span',{'class':'font_black15'})
# print(data4)
# print(' 樂透彩'+ data4[0].text +'期開獎號碼')
