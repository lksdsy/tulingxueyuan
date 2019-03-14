from urllib import request


def spider(url):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'

    # print(user_agent)
    headers = {
        'User-Agent':user_agent
    }

    req = request.Request(url=url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()

    # 文件名
    name = url.split('/')
    fileName = 'lx' + name[-1]

    with open(fileName, 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    url_list = [
        #'http://www.langlang2017.com/index.html'
        #'http://www.langlang2017.com/route.html'
        'http://www.langlang2017.com/FAQ.html'
    ]
    for url in url_list:
        spider(url)




