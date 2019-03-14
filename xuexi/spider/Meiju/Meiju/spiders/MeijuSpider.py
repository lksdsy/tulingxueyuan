# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from xuexi.spider.Meiju.Meiju.items import MeijuSpiderItem

class MeijuspiderSpider(scrapy.Spider):
    name = 'MeijuSpider'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self, response):
        # response.xpath('//ul[@class="top-list  fn-clear"]/li') 返回解析内容的列表
        html = etree.HTML(response.body.decode('GBK'))
        movies = html.xpath('//ul[@class="top-list  fn-clear"]/li')
        for movie in movies:
            name = movie.xpath('./h5/a')[0].text
            srate = movie.xpath('./span[@class="state1 new100state1"]/font')[0].text
            print(name,srate)

            item = MeijuSpiderItem()
            item['name'] = name
            item['state'] = srate

            yield item




