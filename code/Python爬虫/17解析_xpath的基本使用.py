# _*_ utf-8 _*_
# Time : 2022/10/10 23:26
# FILE : 17解析_xpath的基本使用
# PROJECT : Python爬虫
# Author : kkk

from lxml import etree

# xpath 两种解析
# (1)解析本地文件          etree.parse
# (2)解析请求服务器的文件   etree.HTML

# xpath解析本地文件
tree = etree.parse('demo/xpath.html')

# tree.xpath('路径') 在页面过滤内容
# 查找ul下的li列表  路径查询
# liList = tree.xpath('//ul/li')


# 谓词查询 查找有id的li
# text() 获取标签内容
# idLiList = tree.xpath('//ul/li[@id]/text()')
# print(idLiList)

# 找到id为tb1的li标签 注意要加引号
# liList = tree.xpath('//ul/li[@id="tb1"]/text()')

# 属性查询 查询id为tb1的标签的class值
# liList = tree.xpath('//ul/li[@id="tb1"]/@class')

# 模糊查询id里带l的li标签  模糊查询用得不多
# liList = tree.xpath('//ul/li[contains(@id,"t")]/text()')

# 查询id以t开头的li
# liList = tree.xpath('//ul/li[starts-with(@id,"t")]/text()')

# 逻辑查询 查找id="tb1" class="bt1"的li
# liList = tree.xpath('//ul/li[@id="tb1" and @class="bt1"]/text()')

liList = tree.xpath('//ul/li[@id="tb1" or @id="tb2"]/text()')

print(liList)

