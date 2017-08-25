import urllib.request
from html.parser import HTMLParser
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


targetURL = 'http://tw.movie.yahoo.com/movieinfo_main.html/id=5450'
data = urllib.request.urlopen(targetURL)
content = data.read().decode('utf_8')
data.close()
file = open('movie.txt','w',encoding = 'utf_8')

class myparser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.isText = 0
		self.isTextBulletin = 0
		self.isTextFull = 0
		self.Title = ''
		self.MovieInfo = ''
		self.Text = ''

	def handle_data(self, data):
		#片名
		if self.isText == 1:
			self.Title += data
			self.isText = 0
		#資訊
		if self.isText == 2:
			self.MovieInfo += data

		if self.isTextFull == 1:
			self.Text += data

	def handle_starttag(self, tag, attrs):
		if tag == 'div' and attrs == [('class', 'text bulletin')]:
			self.isTextBulletin = 1
		#中文片名
		if self.isTextBulletin == 1 and tag == 'h4':
			self.isText = 1
		#英文片名
		if self.isTextBulletin == 1 and tag == 'h5':
			self.isText = 1
		#電影資訊
		if self.isTextBulletin == 1 and tag == 'span' and attrs == [('class', 'dta')]:
			self.isText = 2
		#電影介紹
		if tag == 'div' and attrs == [('class', 'text full')]:
			self.isTextFull = 1

	def handle_endtag(self, tag):
		if self.isTextBulletin == 1 and tag == 'div':
			self.isTextBulletin = 0

		if self.isTextBulletin == 1 and self.isText == 2 and tag == 'span':
			self.MovieInfo += '\n'
			self.isText = 0

		if self.isTextFull == 1 and tag == 'div':
			self.isTextFull = 0

Parser = myparser()
Parser.feed(content)
file.write(Parser.Title+'\n')
file.write(Parser.MovieInfo)
file.write(Parser.Text)
file.close()
