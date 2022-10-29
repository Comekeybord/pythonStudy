# _*_ utf-8 _*_
# Time : 2022/10/9 16:37
# FILE : 39文件的读写
# PROJECT : code
# Author : kkk

# 写数据
# write方法
# 注意w模式会覆盖原文件的所有内容
# fp = open('demo/test.txt','w')
# fp.write('hello world\n' * 5)
# fp.close()

# a模式不会覆盖，只会追加文件内容
# fp = open('demo/test.txt','a')
# fp.write('hello world\n'*5)
# fp.close()

# read方法读取文件内容 但是是一个字节一个字节读 效率低
fp = open('demo/test.txt','r')
# content = fp.read()
# fp.readline方法只读一行
# content = fp.readline()

# fp.readlines 会以列表的形式返回每一行的内容
content = fp.readlines()
print(content)
