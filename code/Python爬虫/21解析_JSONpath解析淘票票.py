# _*_ utf-8 _*_
# Time : 2022/10/11 16:01
# FILE : 21解析_JSONpath解析淘票票
# PROJECT : Python爬虫
# Author : kkk
import json
import urllib.request

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1665476110278_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-language':'zh-CN,zh;q=0.9,en;q=0.8',
    'bx-v':'2.2.3',
    'cookie':'miid=7726837812014194364; enc=6h4PueMtc088hG9WW1%2B5sUtu3sxOPNWLN1Gi1xsyOPP0MULipphPUPVvhssGFL0YuPBU5doeeiHuP5ijjia2nBuC%2F%2FFfR1llaxR%2F2sFfuzx5FktDdxh1EAWWDbi0HTXg; thw=cn; cna=2EgfG4i2l2ACAT2IzIi9P+hS; t=3f0fe1697ea8edba984347c8ed38554d; cookie2=194713ae17ada878cf1f4e0b4a6444b6; v=0; _tb_token_=e3e9eb83eee3e; xlly_s=1; isg=BEREMFek-3L8f06b7Va83PjbFcI2XWjH0teVAV7lCo_SieVThmhpV4xnySFRkaAf; l=eBxBchuqL9NDpfyvBO5aPurza77TUIRb8sPzaNbMiInca6MCtFToQOCUNofDSdtjgt5eRetPNKfZAdnerxULRFsWHpfuKtyuJe968e1..; tfstk=c8VABETV6gjmn1jiajBobpkPdG_hZ3SojQoH65fqv_EBWjAOiPF39ETl42iEDaC..',
    'referer':'https://dianying.taobao.com/',
    'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-requested-with':'XMLHttpRequest',
}
request = urllib.request.Request(url=url,headers=headers)
content = urllib.request.urlopen(request).read().decode('utf-8')
# 把前面的jsonp和后面的括号去掉
content = content.split('(')[1].split(')')[0]
# 写入文件
with open('demo/taopiaopiao.json', 'w', encoding='utf-8') as fp:
    fp.write(content)


# 获取所有regionName
import jsonpath
taopp = json.load(open('demo/taopiaopiao.json', 'r', encoding='utf-8'))
regionName = jsonpath.jsonpath(taopp, '$..regionName')
print(regionName)
