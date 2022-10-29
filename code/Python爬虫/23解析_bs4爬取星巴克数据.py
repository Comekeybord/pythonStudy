# _*_ utf-8 _*_
# Time : 2022/10/11 19:13
# FILE : 23解析_bs4爬取星巴克数据
# PROJECT : Python爬虫
# Author : kkk

from bs4 import BeautifulSoup
import urllib.request

def getContent():
    url = 'https://www.starbucks.com.cn/menu/'
    res = urllib.request.urlopen(url)
    content = res.read().decode('utf-8')
    return content

def getImg(content):
    soup = BeautifulSoup(content, 'lxml')
    # //ul[@class="grid padded-3 product"]//strong/text()
    # 通过bs4过滤
    nameList = soup.select('ul[class="grid padded-3 product"] strong')
    style = soup.select('ul[class="grid padded-3 product"]>li div')
    for i in range(len(nameList)):
        # 把图片下载到本地
        src = style[i].attrs.get('style')
        imgUrl = 'https://www.starbucks.com.cn' + src.split('"')[1].split('"')[0]
        fileName = 'demo/xinbake/'+str(i)+'.jpg'
        # 下载图片
        urllib.request.urlretrieve(imgUrl, fileName)



if __name__ == '__main__':
    # 获取内容
    content = getContent()
    # 下载图片和名字
    getImg(content)
