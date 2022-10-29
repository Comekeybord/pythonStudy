import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['es.58.com']
    start_urls = ['http://es.58.com/?key=%E5%89%8D%E7%AB%AF']

    def parse(self, response):
        # 获取字符串
        # print(response.text)
        # 获取二进制内容
        # print(response.body)
        # 通过xpath过滤response内容
        print('==============================')
        tagas = response.xpath('//div')[0]
        print(tagas.extract())
