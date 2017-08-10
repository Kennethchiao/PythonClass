import requests
import time
from bs4 import BeautifulSoup
import os
import re
import urllib.request
import json

PTT_URL = 'https://www.ptt.cc'

def get_web_page(url):
    time.sleep(0.5)
    resp = requests.get(url = url, cookies = {'over18':'1'})

    if resp.status_code != 200:
        print("Invalid" , resp.url)
        return None
    else:
        return resp.text

def get_articles(dom, date):
    soup = BeautifulSoup(dom,'html.parser')

    # get next page info
    pre_page = soup.find('div','btn-group btn-group-paging')
    prev_url = pre_page.find_all('a')[1]['href']

    # article info
    articles = []
    divs = soup.find_all('div','r-ent')
    for d in divs:
        if d.find('div','date').string.strip() == date:
            push_count = 0
            if d.find('div','nrec').string:
                try:
                    push_count = int(d.find('div','nrec').string)
                except ValueError:
                    pass
            # get articles link and title
            if d.find('a'):
                href = d.find('a')['href']
                title = d.find('a').string
                articles.append({'title':title, 'href':href , 'push_count':push_count})
    return articles,prev_url

def parser(dom):
    soup = BeautifulSoup(dom,'html.parser')
    links = soup.find(id='main-content').find_all('a')
    img_urls = []
    for link in links:
        if re.match(r'^https?://(i.)?(m.)?imgur.com',link['href']):
            img_urls.append(link['href'])
    return img_urls


def save(img_urls,title):
    if img_urls:
        try:
            # 去除前後空白
            dname = title.strip()
            os.makedirs(dname)
            for img_url in img_urls:
                if img_url.split('//')[1].startswith('m.'):
                    img_url = img_url.replace('//m.','//i.')
                if not img_url.split('//')[1].startswith('i.'):
                    img_url = img_url.split('//')[0]+'//i.'+img_url.split('//')[1]
                if not img_url.endswith('.jpg'):
                    img_url += '.jpg'
                fname = img_url.split('/')[-1]
                urllib.request.urlretrieve(img_url , os.path.join(dname,fname))
                print(fname)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    current_page = get_web_page(PTT_URL + '/bbs/Beauty/index.html')
    if current_page:
        # all article today.
        articles = []
        # format toady date infor cancel '0'
        date = time.strftime("%m/%d").lstrip('0')
        # articles in this page today
        current_articles, prev_url = get_articles(current_page,date)


        while current_articles:
            articles += current_articles
            current_page = get_web_page(PTT_URL + prev_url)
            current_articles , prev_url = get_articles(current_page,date)

        for article in articles:
            print('Processing' , article)
            page = get_web_page(PTT_URL + article['href'])
            if page:
                img_urls = parser(page)
                save(img_urls , article['title'])
                article['num_image'] = len(img_urls)

        with open('DonwloadBeauty.json' , 'w' , encoding = 'utf-8') as f :
            json.dump(articles, f , indent=2 , sort_keys=True ,ensure_ascii=False )
