# -*- coding: utf-8 -*-
import random

import os
from urllib import request

import scrapy
import time

from xuexi.spider.LianjiSpider.LianjiSpider.settings import headers
from xuexi.spider.LianjiSpider.LianjiSpider.items import LianjiaSpiderItem

class LjspiderSpider(scrapy.Spider):
    name = 'LJSpider'
    allowed_domains = ['lianjia.com']
    # start_urls = ['http://lianjia.com/']

    # 定义url地址
    def start_requests(self):
        # start_urls = []
        # for page in range(1,5):
        #     url = 'https://hz.lianjia.com/zufang/binjiang/pg{}rp2rp3'.format(page)
        #     start_urls.append(url)
        start_urls = [
            'https://cd.lianjia.com/zufang/binjiang/l1rp2rp3/',
            'https://cd.lianjia.com/zufang/yuhang/l1rp2rp3/'
        ]
        for start_url in start_urls:
            yield scrapy.Request(url=start_url,callback=self.parse,dont_filter=True,headers=headers)
    def parse(self, response):
        infos = response.xpath('//div[@class="content__list"]/div[@class="content__list--item"]')
        # print(infos)
        for info in infos:
            # 获取房屋名称
            house_titles = info.xpath('.//p[@class="content__list--item--title twoline"]/a/text()').extract()
            house_title = house_titles[0].strip().replace(' ','')
            # print(house_title)

            # 获取房屋详情连接
            house_hrefs = info.xpath('.//p[@class="content__list--item--title twoline"]/a/@href').extract()
            house_href = 'https://hz.lianjia.com'+house_hrefs[0]
            # print(house_href)

            # 获取小区名称
            house_names = info.xpath('.//p[@class="content__list--item--des"]//a/text()').extract()
            house_name = '-'.join(house_names)
            # house_names1 = info.xpath('.//p[@class="content__list--item--des"]//a/text()').extract()
            # house_names2 = info.xpath('.//p[@class="content__list--item--des"]/span/text()').extract_first()
            # if house_names1 == [] and house_names2 != None:
            #     house_name = house_names2
            # elif house_names1 != []:
            #     house_name = '-'.join(house_names1)
            # else:
            #     house_name = '卖没了'
            # print(house_name)
            time.sleep(random.choice([0.5,1,1.5]))
            yield scrapy.Request(url=house_href,callback=self.detail_parse,dont_filter=True,headers=headers,meta={'house_title':house_title,'house_href':house_href,'house_name':house_name})
    def detail_parse(self,response):
        infos = response.xpath('//div[@class="content clear w1150"]')
        for info in infos:
            # 获取房源编号
            house_num = info.xpath('.//i[@class="house_code"]/text()').extract_first()
            # print(house_num)

            # 获取房屋价格
            house_price1 = info.xpath('.//p[@class="content__aside--title"]/span/text()').extract()
            house_price2 = info.xpath('.//p[@class="content__aside--title"]/text()').extract()
            house_price = house_price1[0] + house_price2[0]
            # print(house_price)

            # 获取房屋信息
            house_infos = info.xpath('.//p[@class="content__article__table"]//span/text()').extract()

            # 租聘方式
            house_style = house_infos[0]
            # 厅事
            house_ting = house_infos[1]
            # 大小
            house_size = house_infos[2]
            # 方向
            house_fangxiang = house_infos[3]
            # print(house_style, house_ting, house_size, house_fangxiang)

            # 图片存储地址
            house_imgdir = '/home/tlxy/tulingxueyuan/xuexi/spider/LianjiSpider/ljimg/' + response.meta['house_title']
            # print(house_imgdir)


            # 进行数据存储
            item = LianjiaSpiderItem()

            item['house_title'] =response.meta['house_title']
            item['house_href'] =response.meta['house_href']
            item['house_name'] =response.meta['house_name']
            item['house_num'] =house_num
            item['house_price'] =house_price
            item['house_style'] =house_style
            item['house_ting'] =house_ting
            item['house_size'] =house_size
            item['house_fangxiang'] =house_fangxiang
            item['house_imgdir'] = house_imgdir

            yield item

            # 图片处理
            # house_img_srcs = info.xpath('.//div[@class="content__article__slide__item"]/img/@src').extract()
            # # print(house_img_src)
            #
            # if len(house_img_srcs) != 0:
            #     for house_img_src in house_img_srcs:
            #         # 图片名称
            #         img_name = str(time.time()) + '.jpg'
            #         if not os.path.exists(house_imgdir):
            #             os.makedirs(house_imgdir)
            #         request.urlretrieve(house_img_src,house_imgdir+'/'+img_name)