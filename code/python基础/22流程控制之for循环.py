# _*_ utf-8 _*_
# Time : 2022/10/8 22:27
# FILE : 22流程控制之for循环
# PROJECT : code
# Author : kkk

# 语法:
# for 变量 in 要遍历的数据:
# 循环字符串
# s = 'abcdefg'
# for item in s:
#     print(item)

# range()生成的是一个可以遍历的对象
# range(5) 0~4 左闭右开区间 [0,5)
# for item in range(5):  # 结果是从0到4
#     print(item)

# range(1,6) range(起始值，结束值)
# [1,6) 还是左闭右开
# for item in range(1,6):
#     print(item)

# range(1,10,3) range(起始值，结束值，步长) 左闭右开区间
# for item in range(1, 10, 3):
#     print(item)

# 应用场景： 爬取一个列表返回给我们
# 循环列表
tlist = ['周杰伦','林俊杰','华晨宇']
# len获取元素个数
# print(len(tlist))
# 遍历元素
# for item in tlist:
#     print(item)

# 遍历下标
for i in range(len(tlist)):
    print(i)