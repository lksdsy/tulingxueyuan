# from urllib import request
#
# url = 'http://www.baidu.com'
#
# rsp = request.urlopen(url)
#
# html = rsp.read().decode()
#
# print(html)

from urllib import request,error

try:
    base_url = 'http://www.w3cschool.com.cn/json/index.asp'
    rsp = request.urlopen(base_url)
    html = rsp.read().decode()
    print(html)

except error.HTTPError as e:
    print(e)
except error.URLError as e:
    print(e)
