# -*- coding: utf-8 -*-
import scrapy


class MyhspiderSpider(scrapy.Spider):
    name = 'myhSpider'
    def start_requests(self):
        urls = ['http://lab.scrapyd.cn/page/{}'.format(str(num)) for num in range(1,7)]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]

        filename = 'mingyan-%s'%page

        with open(filename,'wb') as f:
            f.write(response.body)

        self.log("保存文件:%s"%filename)
        # title = response.xpath('//div[@class="quote post"]/span/text()').extract()[0]
        # print(title)