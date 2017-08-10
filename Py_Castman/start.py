import requests
import time
from bs4 import BeautifulSoup

def get_web_page(url):
    resp = requests.get(
    url = url
    )
    if resp.status_code !=200:
        print('Invalid url', resp.url)
        return None
    else:
        return resp.text

def get_articles(dom,date):
    soup  = BeautifulSoup(dom,'html.parser')
    articles = []
    divs = soup.find_all('div','r-ent')
    for d in divs:
        if d.find('div','date').string.strip() == date:
            push_count = 0
            if d.find('div','nrec').string:
                try:
                    push_count = int(d.find('div','nrec').string)
                except ValueError :
                    pass
            if d.find('a'):
                href = d.find('a')['href']
                title = d.find('a').string
                articles.append({
                'title':title , 'href': href , 'push_count':push_count
                })

    return articles
if __name__ == '__main__':
    page = get_web_page('https://www.ptt.cc/bbs/Beauty/index.html')
    if page:
        date = time.strftime("%m/%d").lstrip('0')
        current_articles = get_articles(page,date)
        for post in current_articles:
            print(post)
