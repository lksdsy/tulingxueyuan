# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiciItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class XiciDailiItem(scrapy.Item):
    country = scrapy.Field()
    ipaddress = scrapy.Field()
    port = scrapy.Field()
    serveraddr = scrapy.Field()
    isanonymous = scrapy.Field()
    type = scrapy.Field()
    alivetime = scrapy.Field()
    Verifictiontime = scrapy.Field()


    """
    data["country"] = country
    data["ipaddress"] = item.xpath('./td')[1].text
    data["port"] = item.xpath('./td')[2].text
    data["serveraddr"] = item.xpath('./td')[3].text
    data["isanonymous"] = item.xpath('./td')[4].text
    data["type"] = item.xpath('./td')[5].text
    data["alivetime"] = item.xpath('./td')[6].text
    data["verifictiontime"] = item.xpath('./td')[7].text
    """