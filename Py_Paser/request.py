import requests

# url = 'http://www.yahoo.com.tw'
# html = requests.get(url)
# html.encoding = 'utf-8'
# # print(html.text)
#
# htmllist = html.text.splitlines()
# for row in htmllist:
#    print(row)

url = 'http://www.yahoo.com.tw'
html = requests.get(url)
html.encoding = 'utf-8'
#print(html.text)

htmllist = html.text.splitlines()
times = 0

for row in htmllist:
    #print(row)
    if '世大運' in row:
        times+=1
print('Find {} times'.format(times))
