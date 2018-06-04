# -*- coding: utf-8 -*-
import scrapy
from amazon.items import AmazonItem 


class AmazonspiderSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
        'https://www.amazon.cn/gp/bestsellers/books/ref=sv_b_3',
    ]

    def parse(self, response):
        item = AmazonItem()
        for amazon in response.xpath('//div[@class="a-container"]'):
            item['name'] = amazon.xpath('.//li/a/text()').extract()
            item['author'] = amazon.xpath('.//li/a/text()').extract()
            yield item
            



