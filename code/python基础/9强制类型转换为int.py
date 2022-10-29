# _*_ utf-8 _*_
# Time : 2022/10/8 20:13
# FILE : 9强制类型转换
# PROJECT : code
# Author : kkk


# 注意 字符串中带 . 或 字母 都不能直接转为int类型
# 语法 类型()
# string->int
a = '123'
print(int(a))  # 转换为整形

# float->int 直接去除小数点后面的小数
b = 1.12
print(int(b))

# boolean->int
# 真为1 假为0
c = True
d = False
print(int(c))
print(int(d))
