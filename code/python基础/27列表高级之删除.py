# _*_ utf-8 _*_
# Time : 2022/10/9 12:10
# FILE : 27列表高级之删除
# PROJECT : code
# Author : kkk

# del 删除指定下标的元素
nlist = [1,2,3,4,5]
del nlist[4]
print(nlist)

# pop 删除列表最后一个元素
nlist2 = [1,2,3,4,5]
nlist2.pop()
print(nlist2)

# remove 删除指定元素
nlist3 = [1,2,3,4,5]
nlist3.remove(2)
print(nlist3)