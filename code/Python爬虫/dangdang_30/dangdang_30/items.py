# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Dangdang30Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 在这里定义数据结构  就是要下载哪些数据
    name = scrapy.Field()
    img = scrapy.Field()
    price = scrapy.Field()
