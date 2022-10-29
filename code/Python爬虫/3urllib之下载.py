# _*_ utf-8 _*_
# Time : 2022/10/9 19:04
# FILE : 3urllib之下载
# PROJECT : Python爬虫
# Author : kkk

import urllib.request

# 下载网页
# page_url = 'http://www.baidu.com'
# # 开始下载
# urllib.request.urlretrieve(page_url,'demo/baidu.html')

# 下载图片
# img_url = 'https://img2.baidu.com/it/u=2269866435,461542533&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=489'
# urllib.request.urlretrieve(img_url,'demo/lisa.jpg')


# 下载视频
video_url = 'https://v9-xg-web-pc.ixigua.com/73cb6fdd5cace9c8f3f6d3c3405b81c7/6342c00d/video/tos/cn/tos-cn-ve-4c001-alinc2/e2cfa23de0a94beca50f602c331c5740/?a=1768&ch=0&cr=0&dr=0&er=0&cd=0%7C0%7C0%7C0&cv=1&br=831&bt=831&cs=0&ds=3&ft=Wg3ElNN6Vk3wb8ZHq8dzJLeOYZlcqn2.d2bLn99-puZm&mime_type=video_mp4&qs=0&rc=ZWZmaGc5ZzY1ZTxpPDs7OkBpam9vczw6ZnFxZjMzNDczM0AvLmNjY2BfXjUxXmIzYDBeYSMwaWJscjRnaWhgLS1kLS9zcw%3D%3D&l=20221009192624010212148137065F855A'
urllib.request.urlretrieve(video_url,'demo/video.mp4')

