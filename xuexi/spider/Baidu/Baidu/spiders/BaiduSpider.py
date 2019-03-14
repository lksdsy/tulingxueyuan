# -*- coding: utf-8 -*-
import scrapy


class BaiduspiderSpider(scrapy.Spider):
    # 爬虫名称
    name = 'BaiduSpider'
    # 爬虫允许的域名
    allowed_domains = ['baidu.com']
    # 爬虫的起始url
    start_urls = ['http://baidu.com/']


    # 重写parse 方法
    def parse(self, response):
        with open('baudu.html','w',encoding='utf-8') as f:
            # response.body  网页内容
            f.write(response.body.decode('utf-8'))
