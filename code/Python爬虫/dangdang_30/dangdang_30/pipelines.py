# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import urllib.request



class Dangdang30Pipeline:
    # 管道封装
    # 使用内置打开spider函数和关闭spider时 执行的函数
    def open_spider(self, spider):
        print('+++++++++++++++Dangdang30Pipeline++++++++++++++++')
        self.fp = open('book.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        # 写文件
        self.fp.write(str(item) + ",")

        return item

    def close_spider(self, spider):
        print('------------------------------Dangdang30Pipeline--------------------------------')
        self.fp.close()



# 开启多条管道同步下载
# (1)定义管道类
# (2)在setting中开启管道
class DangDang30ImgPipeline:
    def open_spider(self, spider):
        #
        print('++++++++++++++++DangDang30ImgPipeline++++++++++++++++++++')


    def process_item(self, item, spider):
        imgUrl ='http:' + item.get('img')
        fileName = item.get('name')
        urllib.request.urlretrieve(imgUrl, './books/' + fileName + '.jpg')
        return item


    def close_spider(self, spider):
        print('---------------------------------DangDang30ImgPipeline---------------------------------------')