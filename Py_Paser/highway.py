# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
from html.parser import HTMLParser
data = urllib.parse.urlencode({'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490','EndStation':'f2519629-5973-4d08-913b-479cce78a356','SearchDate':'2015/04/17','SearchTime':'08:00','SearchWay':'DepartureInMandarin','RestTime':'','EarlyOrLater':''})
data = data.encode('utf-8')
request = urllib.request.Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")
response = urllib.request.urlopen(request, data)
html = response.read().decode('utf-8')
file = open('thsrc.html','w',encoding='utf-8')
class myparser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.isNumber = 0
		self.numbers = []
	def handle_data(self, data):
		if self.isNumber == 1:
			print(data)
			self.isNumber = 0
	def handle_starttag(self, tag, attrs):
		#車次
		if tag == 'td' and attrs == [('class','column1')]:
			self.isNumber = 1
		#起始時間
		if tag == 'td' and attrs == [('class','column3')]:
			self.isNumber = 1
		#到達時間
		if tag == 'td' and attrs == [('class','column4')]:
			self.isNumber = 1

Parser = myparser()
file.write(html)
Parser.feed(html)
file.close()
