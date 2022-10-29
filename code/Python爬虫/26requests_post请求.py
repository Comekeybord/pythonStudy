# _*_ utf-8 _*_
# Time : 2022/10/11 21:02
# FILE : 26requests_post请求
# PROJECT : Python爬虫
# Author : kkk

import requests
import json

url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
data = {
    'kw': 'spiderman'
}

res = requests.post(url=url,data=data,headers=headers)
content = res.text
content = json.loads(content.encode('utf-8'))
print(content)
