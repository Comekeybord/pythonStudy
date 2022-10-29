# _*_ utf-8 _*_
# Time : 2022/10/10 20:21
# FILE : 16urllib_代理池
# PROJECT : Python爬虫
# Author : kkk

import random
import urllib.request
import urllib.parse

# 利用列表来创建代理池，绕过封ip
proxiesList = [
    {'http': '61.164.39.68:53281'},
    {'http': '61.216.156.222:60808'},
    {'http': '58.20.184.187:9091'},
    {'http': '39.108.101.55:1080'},
    {'http': '27.42.168.46:55481'},
]
# 准备请求数据
url = 'https://www.baidu.com/s?'
data = {
    'wd': 'ip'
}
data = urllib.parse.urlencode(data)
url = url + data
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
request = urllib.request.Request(url=url,headers=headers)
handler = urllib.request.ProxyHandler()
opener = urllib.request.build_opener(handler)
# 发送请求
res = opener.open(request)
content = res.read().decode('utf-8')
with open('demo/baidu_proxyPools.html', 'w', encoding='utf-8') as fp:
    fp.write(content)

