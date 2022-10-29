import scrapy


class OjSpider(scrapy.Spider):
    name = 'oj'
    allowed_domains = ['211.67.32.63']
    start_urls = ['http://211.67.32.63/problemset.php?page=1']

    def parse(self, response):
        content = response.text
        # problemId //tr[@class="evenrow"or@class="oddrow"]/td[2]/text()
        # problemTitle //tr[@class="evenrow"or@class="oddrow"]/td[3]/text()
        # Source //tr[@class="evenrow"or@class="oddrow"]/td[4]/text()

        trList = response.xpath('//tr[@class="evenrow"or@class="oddrow"]')
        print(trList)
        for tr in trList:
            problemId = tr.xpath('./td[2]/div/text()').extract_first()
            problemTitle = tr.xpath('./td[3]//a/text()').extract_first()
            Source = tr.xpath('./td[4]//a/text()').extract_first()
