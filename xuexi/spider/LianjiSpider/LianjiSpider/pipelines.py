# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
# 写入表格
from openpyxl import Workbook

class LianjispiderPipeline(object):
    def process_item(self, item, spider):
        return item



class LianjiaSpiderJsonPipeline(object):
    def __init__(self):
        self.file = open('lianjia.json','w',encoding='utf-8')
    def process_item(self,item,spider):
        str = json.dumps(dict(item),ensure_ascii=False)
        str = str + '\n'
        self.file.write(str)
        return item
    def close_spider(self,spider):
        self.file.close()


class LianjiaSpiderExcel(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['house_title','house_href','house_name','house_num','house_price','house_style','house_ting','house_size','house_fangxiang','house_imgdir'])

    def process_item(self, item, spider):
        line = [item['house_title'], item['house_href'], item['house_name'],item['house_num'],item['house_price'],item['house_style'],item['house_ting'],item['house_size'],item['house_fangxiang'],item['house_imgdir']]
        self.ws.append(line)
        self.wb.save('lianjia.xlsx')

        return item