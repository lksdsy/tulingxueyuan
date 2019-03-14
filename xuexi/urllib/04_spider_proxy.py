from urllib import request
import random

proxy_list = [
    {'https':'111.197.238.158:9999'},
    #{'http':'61.135.217.7:80'},

    #{'http':'180.167.162.166:8080'}
]

proxy = random.choice(proxy_list)

# 快捷代理管理器
proxy_hander = request.ProxyHandler(proxy)

# 创建网络请求对象opener
opener = request.build_opener(proxy_hander)

url = 'http://www.langlang2017.com'

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv31.0) Gecko/20100101 Firefow/31.0'
    }

req = request.Request(url, headers=headers)

resp = opener.open(req)

html = resp.read().decode()
print(html)


