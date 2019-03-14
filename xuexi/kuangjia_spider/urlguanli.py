'''
url管理器
负责两个变量
    - 已经抓取的url集合
    - 未抓取的url集合

1. 判断是否有待取的url地址       has_new_url()
2. 添加新的url到未爬取的集合中    add_new_url(url) add_new_urls(urls)
3. 获取一个url地址              get_new_url()
4. 获取未爬取的url集合的大小      new_url_size()
5. 获取已爬取的url集合的大小      old_url_size()
'''



class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 未爬取的url集合
        self.old_urls = set()  # 已爬取的url集合

    def has_new_url(self):
        '''
        判断是否有未爬取的url地址
        :return:
        '''
        return self.new_urls_size() !=0

    def get_new_url(self,url):
        '''
        获取一个未爬取的url
        :param url:
        :return:
        '''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.new_urls.add(url)


    def new_urls_size(self):
        '''未爬取的url集合大小'''
        return len(self.new_urls)

    def old_url_size(self):
        '''获取已爬取的url集合大小'''
        return len(self.old_urls)