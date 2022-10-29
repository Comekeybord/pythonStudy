# _*_ utf-8 _*_
# Time : 2022/10/9 20:43
# FILE : 7urllib_post请求百度翻译
# PROJECT : Python爬虫
# Author : kkk

import urllib.request
import urllib.parse
import json
# post请求

# 准备数据
base_url='https://fanyi.baidu.com/sug'
data = {
    'kw': 'spider'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
# post请求数据必须 进行urlencode编码和utf-8编码
data = urllib.parse.urlencode(data).encode('utf-8')
# 定制请求体
request = urllib.request.Request(base_url,data,headers)

# 发送请求
res = urllib.request.urlopen(request)
content = res.read().decode()
# 反序列化
content = json.loads(content)
print(content)
