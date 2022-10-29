# _*_ utf-8 _*_
# Time : 2022/10/11 9:29
# FILE : 解析_浏览器xpath&lxml的etree的xpath配合获取百度一下
# PROJECT : Python爬虫
# Author : kkk

# //input[@id="su"]/text()

import urllib.request
from lxml import etree
url = 'https://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
request = urllib.request.Request(url=url,headers=headers)
res = urllib.request.urlopen(request)
content = res.read().decode('utf-8')
# 通过xpath过滤请求中的数据
tree = etree.HTML(content)
baidu = tree.xpath('//input[@id="su"]/@value')
print(baidu[0])
