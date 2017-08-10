from urllib.parse import urlparse

def attri(o):
    scheme = 'scheme = {}'.format(o.scheme)
    netloc = 'netloc = {}'.format(o.netloc)
    port = 'port = {}'.format(o.port)
    path = 'path = {}'.format(o.path)
    query = 'query = {}'.format(o.query)

    return scheme +'\n' +netloc + '\n' +port +'\n' + path +'\n' + query

url  = 'http://taqm.eap.gov.tw:80/pm25/tw/PM25A.aspx?area=1'
o = urlparse(url)

print(attri(o))
