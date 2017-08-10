import requests

from bs4 import BeautifulSoup

#url = 'http://www.yahoo.com.tw'
#html = requests.get(url)
#sp = BeautifulSoup(html.text,'html.parser')

#detail css

#data1 = sp.select('title')
#data2 = sp.select('#rightdown')
#data3 = sp.select('.title')

# print('[ ' + data1 + ' ]' + ' [ ' + data2 + ' ]' + ' [ ' + data3 + ' ]')
#print(data3)



html_test = """
<html><head><title>Web page</title></head>

<p class = "title"><strong>文件標題</strong></p>
<p class = "story">Once upon... there were three Kindown; there name were
<a href = "http://example.com/Red" class = "student" id = "link1">red</a>
<a href = "http://example.com/Blue" class = "student" id = "link2">blue</a>
<a href = "http://example.com/Green" class = "teacher" id = "link3">green</a>
</p>

<p class = "story" >...</p>
"""


sp = BeautifulSoup(html_test,'html.parser')

print(sp.find('strong'))
print()
print(sp.find_all('a'))
print()
print(sp.find_all("a",{"class":"student"}))
print()
data4 = sp.select('#link3')
print(data4)
print(data4[0])
print(data4[0].text)
