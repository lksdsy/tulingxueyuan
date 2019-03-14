# -*- coding: utf-8 -*-
import os
import scrapy


class LanrentukuSpider(scrapy.Spider):
    name = 'lanrentuku'
    allowed_domains = ['lanrentuku.com']
    start_urls = []
    base_url = 'http://www.lanrentuku.com/vector/flower/p%s.html'
    for page in range(1,2):
        start_urls.append(base_url % page)
    print(start_urls)


    root_dir = 'tuku'
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)


    def parse(self, response):
        pass
