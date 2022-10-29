# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib.request
import requests

class Movietiantang31Pipeline:
    # 下载图片管道
    def open_spider(self, spider):
        print('开始下载图片')

    def process_item(self, item, spider):
        url = item.get('src')
        fileName = item.get('name') + '.jpg'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }
        res = requests.get(url, headers=headers)
        content = res.content
        self.fp = open('movies/' + fileName, 'wb')
        self.fp.write(content)
        return item

    def close_spider(self, spider):
        print('图片下载完成')
        self.fp.close()

class DownLoadMovieName:
    # 下载电影名管道
    def open_spider(self, spider):
        print('开始下载电影名')
        self.fp = open('./movies/movieName.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item) + ',')
        return item


    def close_spider(self, spider):
        print('电影名下载完成')
        self.fp.close()