# -*- coding: utf-8 -*-
import scrapy
from ttmj.ttmj.items import TtmjItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        movies = response.xpath('//div[@class="top-list  fn-clear"]/li')
        for each_movie in movies:
            item = TtmjItem()
            item['name'] = each_movie.xpath('./h5/a/text()').extract()[0]
            yield item
