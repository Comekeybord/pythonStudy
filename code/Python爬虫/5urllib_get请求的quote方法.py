# _*_ utf-8 _*_
# Time : 2022/10/9 20:03
# FILE : 5get请求的quote方法
# PROJECT : Python爬虫
# Author : kkk

# 获取周杰伦的搜索结果
import urllib.request
# 导入 urllib.parse库
import urllib.parse

url = 'https://www.baidu.com/s?wd='

# 定制请求对象
# 定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

# 将周杰伦 进行urlencode编码
name = urllib.parse.quote('周杰伦')

# 生成请求对象
request = urllib.request.Request(url=url+name, headers=headers)

# 发送请求
res = urllib.request.urlopen(request)
content = res.read().decode()
print(content)
