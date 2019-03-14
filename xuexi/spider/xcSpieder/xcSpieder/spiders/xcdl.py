# -*- coding: utf-8 -*-
import scrapy
from xuexi.spider.xcSpieder.xcSpieder.items import XcdlItem

class XcdlSpider(scrapy.Spider):
    name = 'xcdl'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/']

    def parse(self, response):
        # print(response.body.decode('utf-8'))
        item_1 = response.xpath('//tr[@class="odd"]')
        item_2 = response.xpath('//tr[@class=""]')
        items = item_1 + item_2
        # print(items)
        a = 0
        infos = XcdlItem()
        for item in items:
            # 获取国家图片连接
            countries = item.xpath('./td[@class="country"]/img/@src').extract()
            # print(countries)
            if countries != []:
                country = countries[0]
            else:
                country = None

            # 获取 ipaddress
            ipaddress = item.xpath('./td[2]/text()').extract()
            try:
                ipaddress = ipaddress[0]
            except:
                ipaddress = None
            # 获取 port
            port = item.xpath('./td[3]/text()').extract()
            try:
                port = port[0]
            except:
                port = None
            # 获取 serveraddress
            serveraddress = item.xpath('./td[4]/text()').extract()
            try:
                serveraddress = serveraddress[0]
            except:
                serveraddress = None
            # 获取 isanonymous
            isanonymous = item.xpath('./td[5]/text()').extract()
            try:
                isanonymous = isanonymous[0]
            except:
                isanonymous = None
            # 获取 type
            type = item.xpath('./td[6]/text()').extract()
            try:
                type = type[0]
            except:
                type = None
            # 获取 alivetime
            alivetime = item.xpath('./td[7]/text()').extract()
            try:
                alivetime = alivetime[0]
            except:
                alivetime = None
            # 获取 verificationtime
            verificationtime = item.xpath('./td[8]/text()').extract()
            try:
                verificationtime = verificationtime[0]
            except:
                verificationtime = None
            print(ipaddress,port,serveraddress,isanonymous,type,alivetime,verificationtime)
            a += 1

            infos["country"] = country
            infos["ipaddress"] = ipaddress
            infos["port"] = port
            infos["serveraddress"] = serveraddress
            infos["isanonymous"] = isanonymous
            infos["type"] = type
            infos["alivetime"] = alivetime
            infos["verificationtime"] = verificationtime

            yield infos
        print(a)