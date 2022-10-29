# _*_ utf-8 _*_
# Time : 2022/10/9 17:15
# FILE : 40文件的序列化和反序列化
# PROJECT : code
# Author : kkk

# 导入json包
import json
# 定义一个列表
name_list = ['zs','ls','ww']

# 序列化：将内存对象转换为json字符串存储到文件中
# 打开文件
fp = open('demo/test.txt','r')
# json.dumps
# # 序列化
# content = json.dumps(name_list)
# # 写入文件
# fp.write(content)

# json.dump
# 这种方法会把序列化和写入文件合并
# json.dump(name_list,fp)

# 反序列化：将json字符串转换为内存中的对象
# loads
# 读取文件内容
# content = fp.readlines()[0]
# # 转换为python数据对象
# print(json.loads(content))


# load
# 这种方法把读取和转换合并为一步
print(json.load(fp))


# 关闭文件
fp.close()

