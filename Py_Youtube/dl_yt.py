# from pytube import YouTube
#
# yt = YouTube()
# yt.url = "https://www.youtube.com/watch?v=KX7sfaplGEE"
# #
# video = yt.get("mp4","360p")
# # print(yt.filename)
# # yt.set_filename('I_Remaber_U')
# # print(yt.filename)
# video.download()

# encoding: utf-8
import requests
import re
import json
from urllib.parse import urlparse
import shutil

req = requests.get(input("輸入網址："))
# 向一網頁做請求
# print req.text

dic = re.findall("ytplayer.config = ({.*?});", req.text)
# 擷取網頁來源中的字典

js = json.loads(dic[0])
# json 編譯

urls = urlparse.parse_qs(js['args']['url_encoded_fmt_stream_map'])
# 擷取字典中的 url 區塊出來
# dic = re.findall("<script >var ytplayer(.*)</script>", req.text)

for url in urls['url']:
    res = re.search('mime=(.*?)\&', url)
    print (urls['url'].index(url) + int(1) + '.', res.group(1))

req = requests.get(urls['url'][input ("輸入來源數字：") - 1], stream = True)
# 向一來源做請求

f = open(raw_input ("輸入檔名：") + '.mp4', 'wb')
# 開啟新增一檔案

shutil.copyfileobj(req.raw, f)
# 儲存擷取的串流

f.close
# 關閉串流
