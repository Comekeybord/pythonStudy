# _*_ utf-8 _*_
# Time : 2022/10/9 15:09
# FILE : 36函数的参数
# PROJECT : code
# Author : kkk



# 按位置传参
def add(a,b):
    print(a+b)

add(1,2)

# 与js或c不同的地方 多了一个关键字传参 但是基本不用
add(b=1, a=2)