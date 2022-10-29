# _*_ utf-8 _*_
# Time : 2022/10/8 22:06
# FILE : 18逻辑运算符的性能优化
# PROJECT : code
# Author : kkk

a = 10
# a == 10 and print(a) 会执行print
# a < 10 and print(a) 不执行print
# 如果and的左边为false那么后面的语句就不再执行了

# a == 10 or print(a) 不执行print
# a < 10 or print(a) 执行print
# 如果 or 左边为true那么后面的语句就不再执行
