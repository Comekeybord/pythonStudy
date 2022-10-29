# _*_ utf-8 _*_
# Time : 2022/10/9 12:35
# FILE : 29字符串、列表、元组之切片
# PROJECT : code
# Author : kkk

s = 'hello world'
# 还是遵循左闭右开 [0,4)
print(s[0:4])

# s[1:] 从下标为1开始一直到最后
print(s[1:])

# s[:4] [第一个元素:终止元素) 从头到冒号后面的数字开区间
print(s[:4])

# 2为步长 每一次下标都加2
print(s[0:6:2])
