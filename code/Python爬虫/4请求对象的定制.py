# _*_ utf-8 _*_
# Time : 2022/10/9 19:33
# FILE : 4请求对象的定制
# PROJECT : Python爬虫
# Author : kkk
import urllib.request

# https://www.baidu.com/s?wd=周杰伦
# url组成  http/https   www.baidu.com  80/443  s   wd=周杰伦   #
#            协议           主机名       端口   路径    参数    锚点

# http/https 80/443
# mysql 3306
# oracle 1521
# redis 6379
# mongodb 27017

# 定制请求对象
url = 'https://www.baidu.com'
# 伪造 user-agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
# 生成请求头
# 因为参数位置不一样 所以要指定形参
request = urllib.request.Request(url=url,headers=headers)
# 发起请求
res = urllib.request.urlopen(request)
# 读取内容并解码
content = res.read().decode('utf8')
print(content)
