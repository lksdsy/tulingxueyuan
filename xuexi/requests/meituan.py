import requests
from lxml import etree
import json



def xiazai(url,headers):
    res = requests.get(url,headers)
    html = etree.HTML(res.text)

    title = html.xpath('//div[@class="product-grid__item ecol"]/a/@title')

    print(title,len(title))

    price = html.xpath('//div[@class="product-grid__item ecol"]//span[@class="room-prop room-prop--price"]/text()')
    print(price,len(price))
    # 'room-prop room-prop--rating'
    score = html.xpath('//div[@class="product-grid__item ecol"]//span[@class="room-prop room-prop--rating"]/text()')
    score = score[0::2]
    print(score, len(score))

    # with open('meituan.json', 'a', encoding='utf-8') as f:
    #     f.write(title)


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
    }
    url = 'https://phoenix.meituan.com/beijing/pn2/'
    xiazai(url,headers)
