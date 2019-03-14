from urllib import request
import ssl

# ssl免认证
ssl._create_default_https_context = ssl._create_unverified_context

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv31.0) Gecko/20100101 Firefow/31.0'
    }

base_url = 'https://inv-veri.chinatax.gov.cn'

req = request.Request(url=base_url,headers=headers)
rsp = request.urlopen(req)
html = rsp.read().decode()
print(html)

