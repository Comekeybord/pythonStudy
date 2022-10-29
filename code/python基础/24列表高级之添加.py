# _*_ utf-8 _*_
# Time : 2022/10/9 11:34
# FILE : 24列表高级之添加
# PROJECT : code
# Author : kkk

# arr.append 添加到列表最后
arr = [1, 2, 3]
arr.append(4)
print(arr)

# insert 插入
arr1 = [1, 3, 4, 5]
# index的值是 想要插入的那个下标
arr1.insert(1, 2)
print(arr1)

# extend 将一个列表中的元素从后面加到当前列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]
