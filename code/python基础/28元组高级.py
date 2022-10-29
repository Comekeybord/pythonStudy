# _*_ utf-8 _*_
# Time : 2022/10/9 12:26
# FILE : 28元组高级
# PROJECT : code
# Author : kkk

# 元组中的元素是不可以修改的
a_tuple = (1,2,3,4,5)
print(a_tuple)

# 如果只有一个元素的元组要在元素后面加逗号 否则会变成int类型
b_tuple = (1)
print(type(b_tuple))
c_tuple = (1,)
print(type(c_tuple))