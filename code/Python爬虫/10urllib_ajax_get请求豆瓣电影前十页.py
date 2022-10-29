# _*_ utf-8 _*_
# Time : 2022/10/10 11:54
# FILE : 109urllib_ajax_get请求豆瓣电影前十页
# PROJECT : Python爬虫
# Author : kkk
import time
import urllib.request
import urllib.parse

# https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&
# start=20&limit=20
# 观察发现存在 第n页 的起始页码是 (n-1)*20

start_page = int(input('请输入起始页码:'))
end_page = int(input('请输入结束页码:'))


def createRequest(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&'
    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }
    #     url编码data
    data = urllib.parse.urlencode(data)
    url = base_url + data
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    return urllib.request.Request(url=url, headers=headers)


def getContent(request):
    return urllib.request.urlopen(request).read().decode('utf-8')


def writeFile(content, page):
    with open('demo/douban_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


# 分别请求每一页的数据
for page in range(start_page, end_page + 1):
    #   定制第一页的请求对象
    request = createRequest(page)
    #   发送请求并返回内
    #   睡眠一秒
    time.sleep(1)
    content = getContent(request)
    # 写入文件
    writeFile(content, page)
