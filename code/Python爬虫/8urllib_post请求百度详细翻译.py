# _*_ utf-8 _*_
# Time : 2022/10/9 22:45
# FILE : 8urllib_post请求百度详细翻译
# PROJECT : Python爬虫
# Author : kkk
import urllib.parse
import urllib.request
import json
# post方法
# 准备请求包
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
# headers中的cookie 复制过来 通过cookie绕过反爬
headers = {
    'Cookie': 'BIDUPSID=B05CD0769A4E7C72D4C27FABD60489D6; PSTM=1659177246; BAIDUID=2DB34079B7985E4F21E9F78F0608898A:FG=1; BAIDUID_BFESS=2DB34079B7985E4F21E9F78F0608898A:FG=1; ZFY=vXmI:AnIbdLlvZTsSqncVo2CoSXgZS7RYdinqqZvmpuU:C; BA_HECTOR=a52k2h00a025ak2125a161rv1hk5cvj1b; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_PS_PSSID=36544_37561_36884_34812_37403_37405_36786_37071_26350_37344_37364; delPer=0; PSINO=6; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1665319912,1665327372; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1665327381; ab_sr=1.0.1_MmUzYTY0OTU5NDY3MWQ2OGI5ZjBmYTA2NGZiN2ZhNWI2YjFmMDUwMjRmYWJiYTI3NWJmYTUyYzkzNTE4MTkxODE3YTdhMDJjYjVlYzliMzVhNzk3NTc5NDBmZjVlMGIyYzE5ZjA3MGM3OGZhNzA0ZDkzMThmMmUwZjAwYTU4MGI1ODdkZTRhYzYyNzQyYzM1NmUwZTcxZjY3MzZiNTk2OA=='
}
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'spider',
    'simple_means_flag': '3',
    'sign': '63766.268839',
    'token': 'f80ebb5acea055301f0d8cfde854d3f3',
    'domain': 'common',
}
# 编码data
data = urllib.parse.urlencode(data).encode('utf-8')
# 定制请求体
request = urllib.request.Request(url,data,headers)
# 发送请求
content = urllib.request.urlopen(request).read().decode('utf-8')
content = json.loads(content)
print(content)