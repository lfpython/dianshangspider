# -*- coding: utf-8 -*-
import scrapy


class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['search.jd.com']
    start_urls = ['https://search.jd.com/Search?keyword=&enc=utf-8']

    def parse(self, response):

        pass
