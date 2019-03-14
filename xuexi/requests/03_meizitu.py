import requests
from lxml import etree
import os
import time
from bs4 import BeautifulSoup
import re

def mz_spider(base_url,headers):
    res = requests.get(base_url,headers)
    html = etree.HTML(res.text)

    # 获取详情页信息
    img_src = html.xpath('//div[@class="postlist"]/ul/li/a/@href')
    for img_url in img_src:
        # print(img_url)
        img_parse(img_url)

def img_parse(img_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
        'Referer': 'http://www.mzitu.com'
    }
    res = requests.get(img_url, headers)
    html = etree.HTML(res.text)

    # 获取标题
    title = html.xpath('//div[@class="content"]/h2/text()')
    print(title)

    # 获取图片总页数
    page_num = html.xpath('//div[@class="pagenavi"]/a/span/text()')[-2]
    # print(page_num)

    # 拼接图片详情页地址
    # for num in range(1, int(page_num)+1):
    #     img_src = img_url+'/'+str(num)
    #     download_img(img_src,title)
    #     # print(img_src)


# 下载图片
def download_img(img_src, title):
    res = requests.get(img_src)
    html = etree.HTML(res.text)

    # 图片具体连接地址获取
    img_url = html.xpath('//div[@class="main-image"]/p/a/img/@src')[0]

    # 下载路径
    root_dir = 'mz_img'
    img_name = img_url.split('/')[-1]
    # print(img_name)
    # print(title)
    title = title.replace(' ', '')

    root_dir = root_dir + '/' + title
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

    res = requests.get(img_url, headers=headers)

    with open(root_dir + '/' + img_name, 'wb') as f:
        f.write(res.content)
        f.close()
        print(title+'~~'+ img_name + '文件保存成功')


if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
        'Referer':'http://www.mzitu.com'
    }

    for i in range(1,11):
        base_url = 'http://www.mzitu.com/page/{}/'.format(str(i))
        time.sleep(1)
        mz_spider(base_url, headers=headers)
