# _*_ utf-8 _*_
# Time : 2022/10/9 13:33
# FILE : 34字典高级之遍历
# PROJECT : code
# Author : kkk

person = {
    'name': 'zs',
    'age': 18,
    'sex': '男'
}
# 1.遍历字典的key
# person.keys() 获取字典中所有的key
# for key in person.keys():
#     print(key)

# 2.遍历字典的value
# person.values() 获取字典中所有的value
# for value in person.values():
#     print(value)

# 3.遍历字典的key和value
# person.items()
# for key,value in person.items():
#     print(key,value)

# 4.遍历字典的元素
# person.items() 返回所有键值对 遍历时以元组的形式返回每一对键值对
for item in person.items():
    print(item)
