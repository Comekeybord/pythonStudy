# _*_ utf-8 _*_
# Time : 2022/10/10 19:13
# FILE : 12urllib_异常
# PROJECT : Python爬虫
# Author : kkk

import urllib.request
import urllib.error

# 处理异常
# url = 'https://blog.csdn.net/deephub/article/details/126847735'
url = 'https://www.goudan.com'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url,headers=headers)
try:
    res = urllib.request.urlopen(request)
    content = res.read().decode('utf-8')
except urllib.error.HTTPError:
    print('http错误')
except urllib.error.URLError:
    print('url错误')


