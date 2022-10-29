# _*_ utf-8 _*_
# Time : 2022/10/9 12:57
# FILE : 30字典高级之查询
# PROJECT : code
# Author : kkk

person = {
    'name': 'zs',
    'age': 28
}

# 访问person的属性
# print(person['name'])
# print(person['age'])

# 使用[]的方式访问字典中不存在的key 会报错  keyerror
# print(person['sex'])

# 第二种访问元素的方式 get方法
print(person.get('name'))
print(person.get('age'))
# 用get方法获取不存在的key时 会返回none
print(person.get('sex'))