import scrapy
from movietiantang31.items import Movietiantang31Item

class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/oumei/index.html']
    # https://www.ygdy8.net/html/gndy/oumei/list_7_2.html
    # https://www.ygdy8.net/html/gndy/oumei/list_7_3.html
    baseUrl ='https://www.ygdy8.net/html/gndy/oumei/list_7_'
    page = 2

    def parse(self, response):
        print('============================================')
        aList = response.xpath('//a[@class="ulink"][2]')
        for a in aList:
            # 获取名字
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()

            secUrl = 'https://www.ygdy8.net/' + href
            meta = {
                'name': name
            }
            # 打开第二页
            yield scrapy.Request(url=secUrl, callback=self.second_parse, meta=meta)

        if (self.page < 100):
            self.page += 1
            url = self.baseUrl + str(self.page) + '.html'
            # scrapy.Request就是scrapy的get请求
            # callback 就是要执行的函数
            yield scrapy.Request(url=url, callback=self.parse)

    def second_parse(self, response):
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        imgName = response.meta.get('name')
        movie = Movietiantang31Item(src=src, name=imgName)
        # 返回给管道
        yield movie
