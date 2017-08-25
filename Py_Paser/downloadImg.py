import requests as rq , os
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen

os.system('clear')
# 利用 requests 抓取網頁原始碼
url = 'http://www.tooopen.com/img/87.aspx'
html = rq.get(url)
html.encoding="utf-8"

# 利用 BeautifulSoup 解析網頁資料
sp = BS(html.text,'html.parser')

# 建立目錄存圖片
imageDir = "images/"
if not os.path.exists(imageDir):
    os.mkdir(imageDir)
else:
    print('mkdir error')

# 取得標籤
all_link = sp.find_all(['a','img'])

for link in all_link:
    # 讀取 src 和 href
    src = link.get('src')
    href = link.get('href')
    attrs = [src,href]
    for attr in attrs:
        # loading .jpg & .png img-files
        if attr != None and ('.jpg' in attr or '.png' in attr):
            full_path = attr
            # 取得檔案名稱
            filename = full_path.split('/')[-1]
            print(full_path)
            # 存圖
            try:
                image = urlopen(full_path)
                f = open(os.path.join(imageDir,filename),'wb')
                f.write(image.read())
                f.close
            except:
                print('{} 無法讀取！'.format(filename))
