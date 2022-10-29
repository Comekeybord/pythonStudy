# _*_ utf-8 _*_
# Time : 2022/10/11 20:58
# FILE : 25requests_get请求
# PROJECT : Python爬虫
# Author : kkk

import requests

url = 'https://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
data = {
    'wd': '北京'
}
res = requests.get(url=url,params=data,headers=headers)
print(res.text)

# 参数使用params传递
# 参数无需urlencode编码
# 不需要请求对象定制
# ?可以加也可以不加