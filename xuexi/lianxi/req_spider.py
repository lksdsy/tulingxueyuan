import requests
from lxml import etree

url = 'https://requestbin.fullcontact.com/167khfg1?inspect'

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

req = requests.get(url,headers=headers)

html = etree.HTML(req.text)

datas = html.xpath('//div[@class="request-body"]/pre/span/text()')

print(datas)