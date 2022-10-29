# _*_ utf-8 _*_
# Time : 2022/10/10 11:35
# FILE : 9urllib_ajax_get请求豆瓣电影第一页
# PROJECT : Python爬虫
# Author : kkk

import urllib.request

# 准备数据
url = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=20&limit=20'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
# 定制请求对象
request = urllib.request.Request(url=url,headers=headers)
# 发送请求
res = urllib.request.urlopen(request).read().decode('utf-8')

# 写到文件里 必须要utf-8编码否则写入不了
# fp = open('demo/douban.json','w',encoding='utf-8')
# fp.write(res)

# 另一种文件写法 这种写完了会自动关闭文件
with open('demo/douban.json','w',encoding='utf-8') as fp:
    fp.write(res)