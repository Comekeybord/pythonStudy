# _*_ utf-8 _*_
# Time : 2022/10/11 20:41
# FILE : 24requests的基本使用
# PROJECT : Python爬虫
# Author : kkk

import requests


# 一个类型 六个方法
url = 'https://www.baidu.com'

res = requests.get(url)

# 响应的类型为requests.models.Response
print(type(res))

# 设置网页编码格式
res.encoding = 'utf-8'

# res.text获取网页源码
# print(res.text)

# res.content二进制形式的数据
# print(res.content)

# res.url返回请求的地址
# print(res.url)

# res.headers返回响应头
# print(res.headers)

# res.status_code返回状态码
print(res.status_code)

