import scrapy

class sp(scrapy.Spider):
    name = 'lx1'
    start_urls = ['http://lab.scarpyd.cd']

    def parse(self, response):

        mingyan = response.css('div.quote')[0]
        text = mingyan.css('.text::text').extract_first()  # 提取名言
        autor = mingyan.css('.author::text').extract_first()  # 提取作者
        tags = mingyan.css('.tags .tag::text').extract()  # 提取标签
        tags = ','.join(tags)  # 数组转换为字符串

        fileName = '%s-语录.txt' % autor  # 爬取的内容存入文件，文件名为：作者-语录.txt
        with open(fileName, 'a+') as f:


        #f = open(fileName, "wb")  # 追加写入文件
            f.write(text)  # 写入名言内容
            f.write('\n')  # 换行
            f.write('标签：' + tags)  # 写入标签
            #f.close()  # 关闭文件操作