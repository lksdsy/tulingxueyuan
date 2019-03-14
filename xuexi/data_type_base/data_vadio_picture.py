'''
1. 获取到下载文件的URL　　二进制方式下载
urllib模块提供的urlretrieve()
    此方法可以进行音频文件下载
    也支持将远程数据下载到本地

urlretrieve(url, filename=None, reporthook=None, data=None)

    url: 下载的url地址
    filename: 数据存储路径＋文件名
    reporthook: 回调函数，链接上服务器或者相应数据传输下载完毕时触发
                常用：显示当前的下载进度
    data: 返回(filename, headers)元组
'''


from urllib import request
import requests
from lxml import etree
import os

def Schedule(blocknum, blocksize, totalsize):
    '''
    显示下载进度
    :param blocknum:  已经下载的数据块
    :param blocksize: 数据块的大小
    :param totalsize: 远程文件大小
    :return:
    '''
    per = 100.0*blocknum*blocksize/totalsize
    if per>100:
        per = 100
    print('当前下载进度为：{}'.format(per))

url = 'http://www.ivsky.com/tupian/ziranfengguang/'

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

rsp = requests.get(url, headers)
# print(rsp.text)

html = etree.HTML(rsp.text)

img_urls = html.xpath('//div[@class="il_img"]//img/@src')

# print(img_url)
for img_url in img_urls:
    root_dir = 'img'
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
    filename = img_url.split('/')[-1]
    request.urlretrieve(img_url, root_dir+'/'+filename, Schedule)
