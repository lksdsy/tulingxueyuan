from selenium import webdriver
import time
from lxml import etree


driver = webdriver.PhantomJS()

def getPage():
    driver.get('https://www.douyu.com/directory/all')
    time.sleep(5)
    html = driver.page_source

    return html

def paser(html):
    # print(html)
    html = etree.HTML(html)
    room_li = html.xpath('//ul[@class="clearfix play-list x1"]/li')
    # print(len(room_li))
    for room in room_li:
        # print(room)
        # 获取标题
        title = room.xpath('.//h3[@class="ellipsis"]/text()')[0].strip()
        # 获取标签
        tag = room.xpath('.//span[@class="tag ellipsis"]/text()')[0].strip()
        # 获取作者
        try:
            author = room.xpath('.//span[@class="imgbox"]/img/@alt')[0]
        except:
            author = room.xpath('.//span[@class="dy-name ellipsis fl"]/text()')[0]
        print(title,'~~~~',tag,'~~~~',author)

if __name__ == '__main__':
    html = getPage()
    paser(html)