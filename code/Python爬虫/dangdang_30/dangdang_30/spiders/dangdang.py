import scrapy
from dangdang_30.items import Dangdang30Item

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    # 如果要爬取多页数据  allowed_domains只用域名就行了
    allowed_domains = ['search.dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=%BF%C6%BB%C3&page_index=1']

    baseUrl = 'http://search.dangdang.com/?key=%BF%C6%BB%C3&page_index='
    page = 1

    def parse(self, response):
        # pipelines 下载数据的
        # items 定义数据结构的
        # 获取名字 图片 价格
        print('========================================')
        # nameList = response.xpath('//ul[@id="component_59"]/li/a/img/@alt')
        # imgList = response.xpath('//ul[@id="component_59"]/li/a/img/@src')
        # priceList = response.xpath('//ul[@id="component_59"]/li//p[@class="price"]/span[1]/text()')
        lists = response.xpath('//ul[@id="component_59"]/li')
        for li in lists:
            name = li.xpath('./a/img/@alt').extract_first()
            img = li.xpath('./a/img/@data-original').extract_first()
            if(not img):
                img = li.xpath('./a/img/@src').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            # 定义一个book对象 等于用item里的Dangdang30Item类加工后的对象
            book = Dangdang30Item(img=img, name=name, price=price)
            # 通过yield提交到pipelines中进行下载   每一次循环就提交一个
            yield book

#     每一页的业务逻辑都是一样的，所以重复一到一百页就行了
#     https://search.dangdang.com/?key=%BF%C6%BB%C3&page_index=1
#     https://search.dangdang.com/?key=%BF%C6%BB%C3&page_index=2
#     https://search.dangdang.com/?key=%BF%C6%BB%C3&page_index=3
        # 调整page
        if(self.page < 100):
            self.page += 1
            url = self.baseUrl + str(self.page)
            # scrapy.Request就是scrapy的get请求
            # callback 就是要执行的函数
            yield scrapy.Request(url=url, callback=self.parse)