# _*_ utf-8 _*_
# Time : 2022/10/8 20:32
# FILE : 12转换为bool
# PROJECT : code
# Author : kkk

# int -> bool 非0为真
a = 0
print(bool(a))

# float -> bool 非0为真
b = -1.2
print(bool(b))

# string -> bool 非空为真
d = '0'
print(bool(d))

# list -> bool 非空为真
e = [0]
print(bool(e))

# tuple -> bool 非空为假
f = (0,)
print(bool(f))

# dict -> bool 非空为真
g = {
    'name': 'zs',
}
print(bool(g))
