# _*_ utf-8 _*_
# Time : 2022/10/9 16:20
# FILE : 38文件的打开和关闭
# PROJECT : code
# Author : kkk

# 创建文件
# open(文件路径,打开模式) 不能直接创建文件夹
# 模式：
#   w：写入
#   r：只读
# fp = open('test.txt', 'w')
# fp.write('hello world')


# 打开文件
fp = open('demo/test.txt', 'w')
fp.write('im iron man')

# 关闭文件
fp.close()
