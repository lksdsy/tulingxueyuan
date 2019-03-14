'''
url = 'https://search.bilibili.com/all?keyword=%E8%A7%86%E9%A2%91&from_source=banner_search&page=3'
'''

import requests
from lxml import etree



def getInfo(start_page,end_page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19'
    }
    for i in range(start_page,end_page):
        url = 'https://search.bilibili.com/all?keyword=%E8%A7%86%E9%A2%91&from_source=banner_search&page={}'.format(i)
        res = requests.get(url,headers=headers)
        # print(res)
        html = etree.HTML(res.text)
        srcs = html.xpath('//ul[@class="video-contain clearfix"]/li/a/@href')
        titles = html.xpath('//ul[@class="video-contain clearfix"]/li/a/@title')
        print(srcs,titles)

if __name__ == '__main__':
    getInfo(1,2)