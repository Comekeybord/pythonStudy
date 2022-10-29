# _*_ utf-8 _*_
# Time : 2022/10/8 22:50
# FILE : 23字符串高级之操作方法
# PROJECT : code
# Author : kkk

# len 判断字符串长度 还可以判断列表的长度
s = 'china'
# print(len(s))

# s.find 查找第一次出点的下标 不存在就返回-1
# print(s.find('l'))

# s.startswith 判断首字母 返回布尔值
# print(s.startswith('c'))

# s.endswith 判断位字母 返回布尔值
# print(s.endswith('c'))

s1 = 'aaabb'
# s1.count 返回字符出现的次数
print(s1.count('a'))

# s1.replace 替换字符串中所有指定的字符 不修改原字符串
print(s1.replace('a','t'))

s2 = 'A#B#C#D#E'
# split 转换为列表
print(s2.split('#'))

# upper lower 转换为大小写
print(s1.upper())
print(s2.lower())

# s3.strip去除首尾空格
s3 = '        a     a   '
print(s3)
print(s3.strip())

# s1.join方法 一个一个插到后面 用的不多
s4 = 'a'
print(s4.join('abcdefg'))
