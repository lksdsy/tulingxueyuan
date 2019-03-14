import requests
from lxml import etree
from xuexi.data_type_base.hupu_mongo import MongoAPI


def spider(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }
    # 请求页面
    req = requests.get(url,headers=headers)
    html = req.text
    # print(html)
    html = etree.HTML(html)
    return html

# 获取标题
def title_parse(href):
    html = spider(href)
    try:
        t = html.xpath('//div[@class="bbs-hd-h1"]/h1/text()')[0]
    except:
        t = None
    return t


# 解析页面内容
def parse(html):
    # 标题
    # titles = html.xpath('//ul[@class="for-list"]//div[@class="titlelink box"]/a[@class="truetit"]/text()')
    # print(len(titles))
    # 标题和url数量不统一，所以到详情页内拿标题


    # 获取详情页url
    parse_hrefs = html.xpath('//ul[@class="for-list"]//div[@class="titlelink box"]/a[@class="truetit"]/@href')
    # print(parse_hrefs)
    parse_hrefs = ['https://bbs.hupu.com' + href for href in parse_hrefs]
    # print(parse_hrefs)
    # 获取标题
    titles = []
    for href in parse_hrefs:
        titles.append(title_parse(href))

    # print(len(titles),titles)

    # 获取作者
    authors = html.xpath('//div[@class="author box"]/a[@class="aulink"]/text()')
    # print(authors)
    # print(len(authors))

    # 获取发布时间
    times = html.xpath('//div[@class="author box"]/a[2]/text()')
    # print(times)
    # print(len(times))

    # 获取回复浏览数
    datas = html.xpath('//ul[@class="for-list"]//span[@class="ansour box"]/text()')
    # print(datas)
    datas = [x.split('\xa0/\xa0') for x in datas]
    # print(datas)
    # 回复数
    replies = [x[0] for x in datas]
    # 浏览数
    browses = [x[1] for x in datas]
    # print(replies)
    # print(browses)

    # 最后回复时间
    last_times = html.xpath('//div[@class="endreply box"]/a/text()')
    # print(len(last_times), last_times)

    # 最后回复人
    last_people = html.xpath('//div[@class="endreply box"]/span[@class="endauthor "]/text()')
    # print(last_people)

    # print(titles)
    # print(parse_hrefs)
    # print(authors)
    # print(times)
    # print(replies)
    # print(browses)
    # print(last_times)
    # print(last_people)
    # print(len(titles),len(parse_hrefs),len(authors),len(times),len(replies),len(browses),len(last_times),len(last_people))

    items = zip(titles,parse_hrefs,authors,times,replies,browses,last_times,last_people)

    return items


# 数据存储
def data_storage(items):
    # print(items)
    hupu_post = MongoAPI('10.0.2.15',27017,'lx','posts')

    # MongoAPI('10.0.2.15',27017,'hupu','post')
    # titles, parse_hrefs, authors, times, replies, browses, last_times, last_people
    for item in items:
        # print(item)
        hupu_post.add({
            'titles':item[0],
            'parse_hrefs':item[1],
            'authors':item[2],
            'times':item[3],
            'replies':item[4],
            'browses':item[5],
            'last_times':item[6],
            'last_people': item[7],
        })


def main():
    url = 'https://bbs.hupu.com/nba-10'
    html = spider(url)
    data_storage(parse(html))


if __name__ == '__main__':
    main()


