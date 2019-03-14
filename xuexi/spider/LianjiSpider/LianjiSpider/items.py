# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjispiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LianjiaSpiderItem(scrapy.Item):
    house_title = scrapy.Field()
    house_href = scrapy.Field()
    house_name = scrapy.Field()
    house_num = scrapy.Field()
    house_price = scrapy.Field()
    house_style = scrapy.Field()
    house_ting = scrapy.Field()
    house_size = scrapy.Field()
    house_fangxiang = scrapy.Field()
    house_imgdir = scrapy.Field()

