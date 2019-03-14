# -*- coding: utf-8 -*-
import scrapy
from XHspider.items import XhspiderItem

class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/2014.html']

    def parse(self, response):
        infos = response.xpath('//div[@class="item masonry_brick masonry-brick"]')
        print(infos)
        for info in infos:
            title = info.xpath('.//div[@class="title"]/span/a/text()').extract()[0]
            href = info.xpath('.//div[@class="title"]/span/a/@href').extract()[0]
            href = 'http://www.xiaohuar.com' + href
            # print(title,href)

            item = XhspiderItem()
            item['title'] = title
            item['href'] = href

            yield item