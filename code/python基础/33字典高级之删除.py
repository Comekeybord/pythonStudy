# _*_ utf-8 _*_
# Time : 2022/10/9 13:17
# FILE : 33字典高级之删除
# PROJECT : code
# Author : kkk


person = {
    'name': 'zs',
    'age': 18
}
# del
#   删除指定元素
# del person['age']
# print(person)
#   删除整个字典
# del person
# print(person)


# clear
#   清空字典但是保留对象 变成一个空字典
person.clear()
print(person)