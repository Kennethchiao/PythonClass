from pytube import YouTube

# 處理 pytube bug (需要憑證問題)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url =  input("輸入想下載的Youtube影片：")
# yt = YouTube("https://www.youtube.com/watch?v=uWrWBrCHLhI&index=69&list=PLNrEXTZ4tDzJl6qZu16iBNronM-n5ppcC")
yt = YouTube(url)
# Once set, you can see all the codec and quality options YouTube has made
# available for the particular video by printing videos.
print(yt.filename)

# To select a video by a specific resolution and filetype you can use the get
# method.
video = yt.get('mp4', '720p')

# Okay, let's download it! (a destination directory is required)
video.download('/Users/kennethchiao/Desktop/PythonClass/Py_Youtube')
