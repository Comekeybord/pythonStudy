# _*_ utf-8 _*_
# Time : 2022/10/11 23:20
# FILE : 28requests登录古诗文网
# PROJECT : Python爬虫
# Author : kkk

import requests
from bs4 import BeautifulSoup
# 先通过页面源码获取__VIEWSTATE 和 __VIEWSTATEGENERATOR
loginUrl = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
loginRes = requests.get(url=loginUrl, headers=headers)
loginContent = loginRes.text
loginSoup = BeautifulSoup(loginContent, 'lxml')
VIEWSTATE = loginSoup.select('#__VIEWSTATE')[0].attrs.get('value')
VIEWSTATEGENERATOR = loginSoup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')


# 准备验证码
# 因为要保证提交验证码和提交密码是同一次链接  所以需要用session
codeUrl = 'https://so.gushiwen.cn/RandCode.ashx'
session = requests.session()
codeRes = session.get(url=codeUrl,headers=headers)
codeContent = codeRes.content
# 写到文件里
with open('code.jpg', 'wb') as fp:
        fp.write(codeContent)


# 发送请求登录页面
codeName = input('请输入验证码:')
pwdUrl = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
pwdData = {
        '__VIEWSTATE': VIEWSTATE,
        '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': 'qclbyx@qq.com',
        'pwd': '13142cazcT',
        'code': codeName,
        'denglu': '登录',
}
pwdRes = session.post(url=pwdUrl,headers=headers,data=pwdData)
pwdContent = pwdRes.text
with open('gushiwen.html', 'w', encoding='utf-8') as fp:
        fp.write(pwdContent)