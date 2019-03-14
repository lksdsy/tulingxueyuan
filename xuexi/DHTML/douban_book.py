'''
url = https://book.douban.com/subject_search?search_text=python&cat=1001&start=15


'''

from selenium import webdriver
import time
from lxml import etree


def spider(url,i):
    driver = webdriver.PhantomJS()
    driver.get(url)

    time.sleep(5)

    driver.save_screenshot('/home/tlxy/tulingxueyuan/xuexi/DHTML/img/douban_book{}.png'.format(str(i)))

    file_name = '/home/tlxy/tulingxueyuan/xuexi/DHTML/img/douban_book.html'

    with open(file_name,'w',encoding='utf-8') as f:
        f.write(driver.page_source)


    # 解析内容
    parser(file_name)

    driver.quit()

def parser(file_name):

    with open(file_name,'r',encoding='utf-8') as f:
        html = f.read()

    # print(html)
    html = etree.HTML(html)
    print(html)

    # 获取所有book
    books = html.xpath('//div[@class="item-root"]')

    # 获取所有子节点
    for book in books:
        # 封面图片连接
        book_src = book.xpath('./a/img/@src')[0]

        # 书名
        book_name = book.xpath('.//div[@class="title"]/a')[0].text

        # 数的连接
        book_url = book.xpath('.//div[@class="title"]/a/@href')[0]

        # 评分
        book_star = book.xpath('.//span[@class="rating_nums"]')[0].text

        # 作者
        book_author = book.xpath('.//div[@class="meta abstract"]')[0].text

        print(book_src,book_name,book_url,book_star,book_author)

        print('。。。。。。正在抓取豆瓣图书第{}页。。。。。。。。'.format(str(i)))

if __name__ == '__main__':
    for i in range(11):
        url = 'https://book.douban.com/subject_search?search_text=python&cat=1001&start={}'.format(str(i*15))
        spider(url,i)