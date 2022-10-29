# _*_ utf-8 _*_
# Time : 2022/10/10 19:51
# FILE : 14urllib_handler的基本使用
# PROJECT : Python爬虫
# Author : kkk

import urllib.request

url = 'http://www.baidu.com'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url,headers=headers)

# 使用handler
# 创建handler对象
handler = urllib.request.HTTPHandler
# 创建opener对象
opener = urllib.request.build_opener(handler)
# 使用open方法
res = opener.open(request)
content =res.read().decode('utf-8')
print(content)
