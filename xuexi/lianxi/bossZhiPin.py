'''
# 地点：杭州   关键字：爬虫 get
https://www.zhipin.com/job_detail/?query=%E7%88%AC%E8%99%AB&scity=101210100&industry=&position=
https://www.zhipin.com/job_detail/?query=Python&scity=101210100&industry=&position=
https://www.zhipin.com/c101210100/?query=%E7%88%AC%E8%99%AB&page=2&ka=page-2
https://www.zhipin.com/c101210100/?query=%E7%88%AC%E8%99%AB&page=3&ka=page-1
query:爬虫
scity:101210100
industry:
position:
'''
import os
import requests
from lxml import etree
import json

class bossZhiPin(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        }
        self.path = os.getcwd()
        self.file = self.path + '/' + 'boss.json'
        self.fp = open(self.file,'a',encoding='utf-8')
        self.fp.write('\n')

    def get_url(self):
        for i in range(11):
            # python
            # url = 'https://www.zhipin.com/c101210100/?query=python&page={}&ka=page-{}'.format(i,i)
            # 爬虫
            url = 'https://www.zhipin.com/c101210100/?query=%E7%88%AC%E8%99%AB&page={}&ka=page-{}'.format(i,i)
            res = requests.get(url,headers=self.headers)
            # print(html.text)
            self.parse(res)

    def parse(self,res):
        items = []
        html = etree.HTML(res.text)
        all_li = html.xpath('//div[@class="job-list"]/ul//li')
        # print(all_li)
        for each in all_li:
            item = {}

            item['name'] = each.xpath('.//div[@class="job-title"]/text()')[0]
            item['salary'] = each.xpath('.//span[@class="red"]/text()')[0]
            item['exp'] = each.xpath('.//div[@class="info-primary"]/p/text()')[0]
            item['gs_name'] = each.xpath('.//div[@class="company-text"]/h3/a/text()')[0]
            item['address'] = each.xpath('.//div[@class="company-text"]/h3/a/@href')[0]
            item['gs_type'] = each.xpath('.//div[@class="company-text"]/p/text()')[0]
            item['time'] = each.xpath('.//div[@class="info-publis"]/p/text()')[0]
            # print(item)
            items.append(item)
        self.down_load(items)


    def down_load(self,items):
        self.fp.write(json.dumps(items,ensure_ascii=False))
        self.fp.write('\n')
        print("数据已写入到{}文件中······".format(self.file))

    def main(self):
        self.get_url()

if __name__ == '__main__':
    boss = bossZhiPin()
    boss.main()
