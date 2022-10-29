# _*_ utf-8 _*_
# Time : 2022/10/9 12:02
# FILE : 26列表高级之查询
# PROJECT : code
# Author : kkk

# in 判断元素是否在列表中
food_list = ['东坡肉','红烧肘子','可乐鸡']
food = input('你要吃什么:')
if food in food_list:
    print('马上上菜')
else:
    print('没有这个菜')


# not in 判断是否不在 列表中
if food not in food_list:
    print('没有这个菜')
else:
    print('马上上菜')
