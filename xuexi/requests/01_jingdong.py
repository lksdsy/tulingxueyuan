import requests

url = 'http://item.jd.com/1250438.html'

try:
    rsp = requests.get(url)
    # 查看状态码
    print(rsp.status_code)
    # 查看完整url地址
    print(rsp.url)
    # 查看编码类型
    print(rsp.apparent_encoding)
    # 这行代码可以避免乱码
    rsp.encoding = rsp.apparent_encoding

    # 查看响应字符串
    # print(rsp.text)
    # 查看响应字节流
    # print(rsp.content)
    cook = rsp.cookies
    print(cook)
    cookiedick = requests.utils.dict_from_cookiejar(cook)
    print(cookiedick)

except:
    pass
