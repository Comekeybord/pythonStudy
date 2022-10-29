# _*_ utf-8 _*_
# Time : 2022/10/13 15:42
# FILE : 31requests请求电影天堂尝试
# PROJECT : Python爬虫
# Author : kkk

import requests

url = 'https://www.ygdy8.net/html/gndy/oumei/index.html'
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
res = requests.get(url=url, headers=headers)
print(res.text)
