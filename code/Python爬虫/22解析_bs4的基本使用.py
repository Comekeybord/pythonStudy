# _*_ utf-8 _*_
# Time : 2022/10/11 16:41
# FILE : 22解析_bs4的基本使用
# PROJECT : Python爬虫
# Author : kkk

from bs4 import BeautifulSoup

# BeautifulSoup缺点 效率低

# 通过解析本地文件 熟悉bs4用法
# BeautifulSoup默认打开文件的编码格式是gbk
# 读取文件并用beautifulsoup加工为soup对象
soup = BeautifulSoup(open('demo/xpath.html', 'r', encoding='utf-8'), 'lxml')

# 直接通过语法过滤出需要的内容
# 读取第一个匹配的标签
# print(soup.li)
# 获取标签的属性
# print(soup.li.attrs)


# bs4的一些函数  三个

# (1)find 返回匹配的第一个标签
# print(soup.find('li'))

# 找到第一个title为sh的li
# print(soup.find('li', title='sh'))
# 找到class为tb1的第一个li 由于不能与关键字重叠 所以设计的时候为class_
# print(soup.find('li', class_='bt1'))

# (2)find_all 返回所有匹配的标签列表 limit限制找前几个
# print(soup.find_all('li', limit=2))

# 如果想获取多个标签对象 那么在find_all参数里面要填 列表形式的数据
# print(soup.find_all(['li','span','a']))

# (3)select (推荐) 返回所有匹配的标签
# select方法以列表的方式返回数据
# print(soup.select('li'))

# 可以通过类选择器和id选择器选择标签
# print(soup.select('.bt1'))
# print(soup.select('#tb2'))

# 属性选择器
# 查找li中有id的标签
# print(soup.select('li[id]'))

# 查找li中指定id的标齐
# print(soup.select('li[id="tb2"]'))

# 后代选择器与子代选择器 与css3语法相同
# print(soup.select('div li'))
# print(soup.select('ul>li'))

# 找到a标签和li标签的所有对象
# print(soup.select('a,li'))

# 节点信息 获取节点内容
obj = soup.select('#tb1')[0]
# 通过标签获取内容
# 注意：string只能获取当前节点的内容  get_text() (推荐)可以获取所有子节点的内容
# print(obj.string)
# print(obj.get_text())

# 节点属性
# obj.name返回标签名
# print(obj.name)
# obj.attrs返回所有属性值 以字典的形式返回
# print(obj.attrs)

# 获取节点的属性
print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])