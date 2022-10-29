import scrapy


class BaiduSpider(scrapy.Spider):
    # 要爬取的名字
    name = 'baidu'
    # 允许爬取的域名
    allowed_domains = ['www.baidu.com']
    # 起始爬取的域名
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print('请求成功')
