# _*_ utf-8 _*_
# Time : 2022/10/9 18:30
# FILE : 1urllib基本使用
# PROJECT : Python爬虫
# Author : kkk
import base64
# 导入urllib的request模块
import urllib.request

# 使用urllib获取百度首页源码
# 定义一个url
url = 'http://www.baidu.com'

# 模拟浏览器向服务器发请求
response = urllib.request.urlopen(url)

# 获取响应中的页面源码
# read方法返回的是字节形式的二进制数据
# 二进制数据->字符串  解码 decode()

content = response.read().decode('utf-8')

# 打印数据
print(content)


