# _*_ utf-8 _*_
# Time : 2022/10/11 13:12
# FILE : 20解析_JSONpath的基本使用
# PROJECT : Python爬虫
# Author : kkk

# 注意：jsonpath只能读取本地文件的内容

import jsonpath
import json

# 导入json文件
obj = json.load(open('demo/20解析_jsonpath.json', 'r', encoding='utf-8'))

# 书店所有作者
authorList = jsonpath.jsonpath(obj, '$.store.book[*].author')
print(authorList)

# 所有的作者
allAuthor = jsonpath.jsonpath(obj, '$..author')
print(allAuthor)

# store下的所有元素
storeElement = jsonpath.jsonpath(obj, '$.store.*')
print(storeElement)

# store下所有的price
storePrice = jsonpath.jsonpath(obj, '$.store..price')
print(storePrice)

# 第三本书
threeBook = jsonpath.jsonpath(obj, '$.store..book[2]')
print(threeBook)

# 最后一本书
lastBook = jsonpath.jsonpath(obj, '$.store..book[(@.length-1)]')
print(lastBook)

# 前两本书
# firstTwoBooks = jsonpath.jsonpath(obj ,'$..book[0,1]')
firstTwoBooks = jsonpath.jsonpath(obj, '$..book[:2]')  # 类似于切片
print(firstTwoBooks)

# 过滤出所有包含isbn的书 条件过滤需要添加?
isbnBook = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
print(isbnBook)

# 哪本书超过了10块钱
tenrmbBook = jsonpath.jsonpath(obj, '$..book[?(@.price>10)]')
print(tenrmbBook)
