# _*_ utf-8 _*_
# Time : 2022/10/10 19:25
# FILE : 13urllib_微博的cookie登录
# PROJECT : Python爬虫
# Author : kkk

# cookie 与 referer
import urllib.request
url = 'https://weibo.com/ajax/profile/info?uid=6569563534'
headers = {
    'cookie': 'PC_TOKEN=26ae921839; XSRF-TOKEN=vKcvnjaLVNjvU9hE0SdIvDsl; SUB=_2A25OQHSyDeRhGeBL7VsU9i3JyDiIHXVtNOF6rDV8PUNbmtANLWzMkW9NRvFL2UyxjrQ4EWNHv0Usl2wrkMx4l6gr; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFLwMgFgQbewl1o6.49S.K55JpX5KzhUgL.FoqfSo.fSoefe0B2dJLoI0jLxKnL1KqL1-zLxK-LB--L1-2LxKnLBo5L1KBLxKqL1h5L1h2LxKqL1hnL1K5LxK-L122L1-qR1hM0S7tt; ALF=1696938081; SSOLoginState=1665402082; WBPSESS=GycniDoMI2GNbRChYmuuzesSb1UlhDkgguL82W9RzOEIgUQMSMsleBOsNs8ewYj2ZMZQ0o8fjuXtS_OLqNKDCPzunzHYMwTQ97v0YNG9ZA_DTHfot1yLZ_eA8g5_vU1SJKlKu_8hoy_1p7GTuIqwrw==',
    'referer': 'https://weibo.com/u/6569563534',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url,headers=headers)
res = urllib.request.urlopen(request)
content = res.read().decode('utf-8')

# 写文件
with open('demo/weibo.json', 'w', encoding='utf-8') as fp:
    fp.write(content)