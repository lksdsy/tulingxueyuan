# -*- coding: utf-8 -*-
import scrapy
from xici.items import XiciDailiItem


class XcdlSpider(scrapy.Spider):
    name = 'xcdl'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/']

    def parse(self, response):
        # print(response.text)
        data = XiciDailiItem()
        items1 = response.xpath('//tr[@class="odd"]')
        items2 = response.xpath('//tr[@class=""]')
        items = items1 + items2
        # print(items)
        for item in items:
            # print(item.xpath('./td[2]').extract()[0])
            # 国家图片链接
            countrys = item.xpath('./td[@class="country"]/img/@src').extract()
            if countrys != []:
                country = countrys[0]
            else:
                pass
            # print(country)

            ipaddress = item.xpath('./td[2]').extract()[0].lstrip("<td>").rstrip("</td>")
            port = item.xpath('./td[3]').extract()[0].lstrip("<td>").rstrip("</td>")
            serveraddr = item.xpath('./td[4]').extract()[0].lstrip("<td>").rstrip("</td>")
            # isanonymous = item.xpath('./td[5]').extract()[0].lstrip("<td>").rstrip("</td>").lstrip('class="country">')
            isanonymous = item.xpath('./td[5]').extract()[0].lstrip('<td class="country">').rstrip("</td>")

            # print(isanonymous)
            type = item.xpath('./td[6]').extract()[0].lstrip("<td>").rstrip("</td>")
            alivetime = item.xpath('./td[7]').extract()[0].lstrip("<td>").rstrip("</td>")
            Verifictiontime = item.xpath('./td[8]').extract()[0].lstrip("<td>").rstrip("</td>")

            # ipaddress,port,serveraddr,isanonymous,type,alivetime,verifictiontime
            print(country,ipaddress,port,serveraddr,isanonymous,type,alivetime,Verifictiontime)
            data["country"] = country
            data["ipaddress"] = ipaddress
            data["port"] = port
            data["serveraddr"] = serveraddr
            data["isanonymous"] = isanonymous
            data["type"] = type
            data["alivetime"] = alivetime
            data["Verifictiontime"] = Verifictiontime

            yield data
