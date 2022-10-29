# _*_ utf-8 _*_
# Time : 2022/10/9 17:46
# FILE : 41异常处理
# PROJECT : code
# Author : kkk

# 读取一个不存在的文件 处理文件找不到的异常
# try:
#     可能错误的代码
# except 错误类型:
#     提示用户

try:
    fp = open('text.txt','r')
except FileNotFoundError:
    print('请检查文件名!')
