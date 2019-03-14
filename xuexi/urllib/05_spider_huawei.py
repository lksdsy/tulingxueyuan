'''
urllib模拟登录华为官网
url = https://www.huawei.com/en/accounts/LoginPost
method=post
parm(参数):
    userName:1541623372@qq.com
    pwd:EXPxI8pSarludCw5s7eHVsf9U8mvV5g7PULqodFhQMsAljNiHeXI6Y/MldeCQLLOzpJUpXwXOpTj+Rbtvz3fwpXrG9ZZOQFwpUMO7n2n5qSHY9isK7W+ZtGCi4TEbbzELDM14LoECuXcBDc8rLzyypscxsXmm4bPCl0x3qO6v7A=
    languages:zh
    fromsite:www.huawei.com
    authMethod:password

'''

from urllib import request,parse
from http import cookiejar

# 生成cookie对象
cookie = cookiejar.CookieJar()

# 生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 生成HTTP请求管理器
http_handler = request.HTTPHandler()
# 生成https管理器
https_handle = request.HTTPSHandler()

# 构建发起请求管理器
opener = request.build_opener(cookie_handler, http_handler, https_handle)

# 构建登录函数
def login(url):
    data = {
        'userName':'yuxiang000',
        'pwd':'Huawei12#$',
        'languages':'zh',
        'fromsite':'www.huawei.com',
        'authMethod': 'password'
    }
    data = parse.urlencode(data)
    req = request.Request(url,data=bytes(data,'utf-8'))
    content = opener.open(req)
    content = content.read().decode()
    print(content)
if __name__ == '__main__':
    url = 'https://www.huawei.com/en/accounts/LoginPost'
    login(url)
