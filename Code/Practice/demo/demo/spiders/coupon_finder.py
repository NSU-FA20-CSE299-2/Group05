import scrapy


class CouponFinderSpider(scrapy.Spider):
    name = 'coupon_finder'
    allowed_domains = ['https://kupwon.com/']
    start_urls = ['http://https://kupwon.com//']

    def parse(self, response):
        pass
