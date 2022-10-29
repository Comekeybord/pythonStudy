# _*_ utf-8 _*_
# Time : 2022/10/8 21:49
# FILE : 13算术运算符
# PROJECT : code
# Author : kkk

# 算术运算符
a = 3
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
# // 整除
print(a // b)
# ** 指数运算
print(a**b)
# () 优先运算
print((a+b)*b)

# 字符串相加 跟js一样 字符串用+拼接
c = '123'
d = '456'
print(c+d)

# 字符串和int类型不能+运算 否则报错
e = 46
print(c+str(e))

# 字符串乘法 字符串会被输出n次
f = 'hello world\n'
print(f*3)