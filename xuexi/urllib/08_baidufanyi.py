from urllib import request,parse
import json
def bd_fanyi(content):
    # 参数封装
    data = {
        'kw':content
    }

    # 参数拼接转码
    data = parse.urlencode(data)

    # 请求地址
    base_url = 'https://fanyi.baidu.com/sug'

    # headers
    headers = {
        'Content-Length':len(data),
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }

    req = request.Request(url=base_url, data=bytes(data, encoding='utf-8'), headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()

    # 使用json格式化数据
    json_data = json.loads(html)
    # print(json_data)
    for item in json_data['data']:
        print(item['k'],item['v'])


if __name__ == '__main__':
    content = input('请输入想要翻译的内容：')
    bd_fanyi(content)