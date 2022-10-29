# _*_ utf-8 _*_
# Time : 2022/10/11 9:41
# FILE : 19解析_获取站长素材图片
# PROJECT : Python爬虫
# Author : kkk

import urllib.request
from lxml import etree



def createRequest(page):
    if (page == 1):
        url = 'https://sc.chinaz.com/tupian/xingganmeinvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/xingganmeinvtupian_' + str(page) + '.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def getContent(request):
    content = urllib.request.urlopen(request).read().decode('utf-8')
    print(content)
    return content

def downImg(content):
    # 通过xpath获取content中的图片的alt和src
    tree = etree.HTML(content)
    alt = tree.xpath('//div[@class="tupian-list com-img-txt-list"]//img/@alt')
    src = tree.xpath('//div[@class="tupian-list com-img-txt-list"]//img/@data-original')
    for i in range(len(alt)):
        # 准备写文件
        name = alt[i]
        baseUrl = src[i]
        url = 'https:'+baseUrl
        # urllib.request.urlretrieve(url,filename)下载图片
        filename = name + '.jpg'
        urllib.request.urlretrieve(url=url,filename='./demo/'+filename)

if __name__ == '__main__':
    start_page = int(input('请输入起始页:'))
    end_page = int(input('请输入结束页:'))

    for page in range(start_page, end_page + 1):
        # 定制请求体
        request = createRequest(page)
        # 获取网页源码
        content = getContent(request)
        # 下载图片
        downImg(content)