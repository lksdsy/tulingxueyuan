'''
url = 'https://www.duitang.com/search/?kw=%E7%BE%8E%E5%A5%B3&type=feed'
Ajax:
    url = 'https://www.duitang.com/napi/blog/list/by_search/?kw=%E7%BE%8E%E5%A5%B3&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&start=24&_=1543900808449'
    url = 'https://www.duitang.com/napi/blog/list/by_search/?kw=%E7%BE%8E%E5%A5%B3&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&start=48&_=1543900808450'
    url = 'https://www.duitang.com/napi/blog/list/by_search/?kw=%E7%BE%8E%E5%A5%B3&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&start=72&_=1543900808451'
    url = 'https://www.duitang.com/napi/blog/list/by_search/?kw=%E7%BE%8E%E5%A5%B3&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&start=96&_=1543900808452'
    url = '                                                  kw:美女                type:feed include_fields:top_comments,  is_root,  source_link,  item,  buyable,  root_id,  status,  like_count,  like_id,  sender,  album,  reply_count,  favorite_blog_id _type: start:24 _:1543902631345'
    url = 'https://www.duitang.com/napi/blog/list/by_search/?kw=%E7%BE%8E%E5%A5%B3&type=feed&_type=&start=96&_=1543900808452'

第二页
    url = 'https://www.duitang.com/napi/blog/list/by_search/?kw=%E7%BE%8E%E5%A5%B3&start=120'
'''


import requests,time,os
from lxml import etree


def dt_spider(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }
    # 请求页面
    req = requests.get(url,headers=headers)
    # print(req.text)
    html = etree.HTML(req.text)
    return html

# 解析页面及获取数据
def parse(html):
    # 获取图片url地址
    img_urls = html.xpath('//div[@class="mbpho"]/a/img/@src')
    # print(img_urls)
    # print(len(img_urls))
    url_list = []
    for title_url in img_urls:
        title_url = title_url.split('/')[5]
        url_list.append(title_url)

    # 获取标题
    titles = html.xpath('//div[@class="wooscr"]/ul/li/p/a/text()')
    # print(titles)
    # print(len(titles))
    n = 0
    title_list = []
    for title in titles:
        title = title + url_list[n]
        n += 1
        title_list.append(title)
        # print(title)

    items = zip(title_list,img_urls)
    return items



# 数据存储
def tpdownload(items):
    root_dir = 'mv_img'
    for item in items:
        # print(item[0],item[1])
        root_dir = root_dir + '/'
        if not os.path.exists(root_dir):
            os.makedirs(root_dir)
        rsp = requests.get(item[1])
        with open(root_dir + '/' + item[0] + '.jpeg', 'wb') as f:
            f.write(rsp.content)
            f.close()
            print(item[0] + '~~' +  '文件保存成功')

def main():
    urls = ['https://www.duitang.com/search/?kw=%E7%BE%8E%E5%A5%B3&type=feed&_type=&start={}&_={}'.format(i * 24, int(
        time.time() * 1000)) for i in range(0, 1)]
    for url in urls:

        tpdownload(parse(dt_spider(url)))


if __name__ == '__main__':
    main()
