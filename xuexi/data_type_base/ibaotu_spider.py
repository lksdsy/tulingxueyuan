import requests
from lxml import etree


class Spider(object):
    def __init__(self):
        self.headers = headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
        self.offset = 1


    def start(self, url):
        res = requests.get(url=url,headers=self.headers)
        html = res.text

        html = etree.HTML(html)

        return html

    def parse(self,html):
        titles = html.xpath('//div[@class="show-image"]/img/@alt')
        # print(titles)
        urls = html.xpath('//div[@class="video-play"]/video/@src')
        # print(urls)

        self.write_file(titles,urls)

    def write_file(self,titles,urls):
        for title,url in zip(titles,urls):
            response = requests.get('http:'+url,headers=self.headers)
            filename = title + '.mp4'

            with open('/home/tlxy/tulingxueyuan/xuexi/data_type_base/movie/'+filename,'wb') as f:
                f.write(response.content)







if __name__ == '__main__':
    spider = Spider()
    for i in range(1,5):
        url = 'https://ibaotu.com/shipin/7-0-0-0-0-{}.html'.format(str(i))
        html = spider.start(url)
        spider.parse(html)