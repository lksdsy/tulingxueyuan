import scrapy
from sp5.items import Sp5Item

class tupian(scrapy.Spider):
    name = 'lx5'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        item = Sp5Item()  # 实例化item
        imgurls = response.css(".post img::attr(src)").extract() # 注意这里是一个集合也就是多张图片
        item['tupian'] = imgurls
        yield item
        pass