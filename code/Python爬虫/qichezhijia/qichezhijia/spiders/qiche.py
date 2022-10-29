import scrapy


class QicheSpider(scrapy.Spider):
    name = 'qiche'
    allowed_domains = ['sou.autohome.com.cn']
    start_urls = ['https://sou.autohome.com.cn/zonghe?q=%B1%A6%C2%ED&pvareaid=100834&entry=42&clubClassBefore=&IsSelect=&clubOrder=&clubClass=&clubSearchType=&clubSearchTime=&pq=%C0%BC%B2%A9%BB%F9%C4%E1%B4%F3%C5%A3&pt=638011990246085000']

    def parse(self, response):
        print('===============================')
        # 获取车名和价格
        nameList = response.xpath('//a[@class="name hoveraddunderline"]/text()')
        priceList = response.xpath('//a[@class="price hoveraddunderline"]/text()')
        for i in range(len(nameList)):
            name = nameList[i].extract()
            price = priceList[i].extract()
            print(name, ':', price)