# _*_ utf-8 _*_
# Time : 2022/10/9 20:26
# FILE : 6get请求的urlencode方法
# PROJECT : Python爬虫
# Author : kkk

# urlencode用在多个参数的请求url中

# 导入要用的包
import urllib.request
import urllib.parse

# 准备数据
base_url = 'https://www.baidu.com/s?'
data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '台湾省'
}
# 拼接请求地址
url = base_url + urllib.parse.urlencode(data)


# 定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url,headers=headers)
# 发送请求
res = urllib.request.urlopen(request)
content = res.read().decode('utf-8')
print(content)