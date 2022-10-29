# _*_ utf-8 _*_
# Time : 2022/10/10 12:39
# FILE : 11urllib_ajax_post请求肯德基官网
# PROJECT : Python爬虫
# Author : kkk
import time
# 发送post请求前十页数据

import urllib.request
import urllib.parse


def createRequest(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '杭州',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=base_url,data=data,headers=headers)
    return request

def getContent(request):
    content = urllib.request.urlopen(request).read().decode('utf-8')
    return content

def writeFile(content,page):
    with open('demo/kendeji_'+ str(page) + '.json',encoding='utf-8',mode='w') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始页:'))
    end_page = int(input('请输入结束页:'))

    for page in range(start_page, end_page + 1):
        # 创建请求对象
        request = createRequest(page)
        # 发送请求
        content = getContent(request)
        # 写文件
        writeFile(content,page)
        # 睡眠一秒
        time.sleep(1)

print("OK")