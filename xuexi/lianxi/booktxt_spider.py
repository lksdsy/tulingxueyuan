import requests
import os
from lxml import etree
import time


'''
url = 'https://www.booktxt.net/0_67/'


'''


headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
    'Referer':'https://www.booktxt.net/0_67/2085805.html'
}


# 主页
def bk(url):
    rsp = requests.get(url, headers=headers)
    rsp.encoding = 'gbk'
    html = etree.HTML(rsp.text)
    # 分页地址
    bk_urls= html.xpath('//div[@id="list"]/dl/dd/a/@href')
    for i in bk_urls:
        bk_url = 'https://www.booktxt.net/0_67/' + i
        # print(bk_url)
        fenye(bk_url)


# 分页及下载
def fenye(url):
    rsp = requests.get(url,headers=headers)
    rsp.encoding = 'gbk'
    time.sleep(1)
    html = etree.HTML(rsp.text)
    # 分页标题
    bk_name = html.xpath('//div[@class="bookname"]/h1/text()')[0]
    # print(bk_name)
    # 内容
    nr = html.xpath('//div[@id="content"]/text()')
    # print(nr)


    # 下载
    with open('zetianji.txt', 'a+') as f:
        f.write(bk_name +'\n')
        # 处理内容
        for x in nr:
            x.replace('\xa0\xa0\xa0\xa0', '\n')
            f.write(x)
        f.close()
        print(bk_name + '下载成功')








if __name__ == '__main__':
    home_url = 'https://www.booktxt.net/0_67/'
    bk(home_url)


