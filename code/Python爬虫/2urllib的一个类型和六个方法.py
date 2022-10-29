# _*_ utf-8 _*_
# Time : 2022/10/9 18:44
# FILE : 2urllib的一个类型和六个方法
# PROJECT : Python爬虫
# Author : kkk

# 导入包
import urllib.request

url = 'http://www.baidu.com'
# 一个类型
res = urllib.request.urlopen(url)
# 返回的类型是 HTTPResponse 类型
# print(type(res))


# 六个方法
# read方法 一个字节一个自己读
# print(res.read())

# read(字节数) 指定读取的字节数
# print(res.read(5))

# readline 一次读取一行
# print(res.readline())

# readlines 读取所有行
print(res.readlines())

# getcode 获取状态码
# print(res.getcode())

# geturl 获取url地址
# print(res.geturl())

# getheaders 获取响应头信息
print(res.getheaders())