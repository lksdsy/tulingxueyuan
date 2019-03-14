'''
https://tieba.baidu.com/f?ie=utf-8&kw=%E9%87%91%E5%BA%B8&fr=search
https://tieba.baidu.com/f?kw=%E9%87%91%E5%BA%B8&ie=utf-8&pn=50
https://tieba.baidu.com/f?kw=%E9%87%91%E5%BA%B8&ie=utf-8&pn=100
'''

from urllib import request,parse

url = 'https://tieba.baidu.com/f?'
name = input('请输入贴吧名称:')
page = int(input('请输入贴吧页数:'))

for i in range(page):
    kw = {
        'kw':name,
        'pn':i*50
    }
    kw_data = parse.urlencode(kw)

    url = url + kw_data


    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv31.0) Gecko/20100101 Firefow/31.0'
    }

    req = request.Request(url, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    with open(name+'第'+str(i+1)+'页'+'html', 'w', encoding='utf-8') as f:
        f.write(html)