import scrapy


class DemoSpiderSpider(scrapy.Spider):
    name = 'demo_spider'
    allowed_domains = ['https://kupwon.com/']
    start_urls = ['http://https://kupwon.com//']

    def parse(self, response):
        pass
