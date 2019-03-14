'''
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
request headers:
    Accept:application/json, text/javascript, */*; q=0.01
    # Accept-Encoding:gzip, deflate    这有毒
    Accept-Language:zh-CN,zh;q=0.9
    Connection:keep-alive
    Content-Length:200
    Content-Type:application/x-www-form-urlencoded; charset=UTF-8
    Cookie:OUTFOX_SEARCH_USER_ID=93468727@10.168.8.76; JSESSIONID=aaaKEe-1E-vCmbCFaN0Cw; OUTFOX_SEARCH_USER_ID_NCOO=1795706165.901427; ___rl__test__cookies=1542776270454
    Host:fanyi.youdao.com
    Origin:http://fanyi.youdao.com
    Referer:http://fanyi.youdao.com/
    User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36
    X-Requested-With:XMLHttpRequest
data:
    i:girl   传入参数
    from:AUTO
    to:AUTO
    smartresult:dict
    client:fanyideskweb
    salt:1542776270466
    sign:5dde1aa5805bb17034577603d887b942
    doctype:json
    version:2.1
    keyfrom:fanyi.web
    action:FY_BY_REALTIME
    typoResult:false

salt:  var t = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
                    时间戳 time.tiem()             0-10随机整数 random.randint(0-10)
sign:  sign: n.md5("fanyideskweb" + e +    t + "sr_3(QOHT)L2dx#uuGR@r")
                md5:hashlib包      传入参数  salt

'''


from urllib import request,parse
import time
import json
import random
import hashlib

# md5加密
def md5js(value):
    md5 = hashlib.md5()
    md5.update(bytes(value, encoding='utf-8'))
    sign =md5.hexdigest()

    return sign

# 解析json
def jsparse(html):
    data_json = json.loads(html)
    sr_json = data_json['smartResult']
    items = sr_json['entries']
    print(items)

def yd_cidian(key):

    base_url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    # salt
    t = int(time.time()*1000) + random.randint(0, 10)

    # sign
    # n.md5("fanyideskweb" + e + t + "sr_3(QOHT)L2dx#uuGR@r")
    new_sign = "fanyideskweb" + key + str(t) + "sr_3(QOHT)L2dx#uuGR@r"


    data = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': t,
        'sign': md5js(new_sign),
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false'
    }

    data = parse.urlencode(data)

    headers = {

                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Accept-Language': 'zh-CN, zh;q=0.9',
                   'Connection': 'keep-alive',
                   'Content-Length': len(data),
                   'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                   'Cookie': 'OUTFOX_SEARCH_USER_ID = 93468727 @10.168.8.76;JSESSIONID = aaaKEe-1E-vCmbCFaN0Cw;OUTFOX_SEARCH_USER_ID_NCOO=1795706165.901427;___rl__test__cookies=1542776270454',
                   'Host': 'fanyi.youdao.com',
                   'Origin': 'http://fanyi.youdao.com',
                   'Referer': 'http://fanyi.youdao.com/',
                   'User-Agent': 'Mozilla/5.0(X11;Linux x86_64)AppleWebKit/537.36(KHTML,likeGecko) Chrome/64.0.3282.119Safari/537.36X-Requested-With:XMLHttpRequest'
    }

    req = request.Request(url=base_url, data=bytes(data, encoding='utf-8'), headers=headers)

    rsp = request.urlopen(req)
    html = rsp.read().decode()
    # jsparse(html)
    print(html)


if __name__ == '__main__':
    key = input('请输入想要翻译的单词(q退出):')

    yd_cidian(key)


