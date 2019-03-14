'''
url = 'http://api.map.baidu.com/place/v2/detail?'


'''
import requests,json
from xuexi.baiduMap_API.MysqlAPI import Sql

def getjson(uid):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    data = {
        'uid':uid,
        'scope':'2',
        'output':'json',
        'ak':'gXaG3THhX2OO20c2T8eUMIHHe8X528GQ',
    }
    url = 'http://api.map.baidu.com/place/v2/detail'
    res = requests.get(url,params=data,headers=headers)
    decodejson = res.json()
    return decodejson

# 从数据库中得到uid号
results = Sql.read_city()
# print(results)
# print(type(results[0])) # 元组类型
for item in results:
    # print(item)
    uid = item[0]
    # print(uid,type(uid))
    decodejson = getjson(uid)
    # print(decodejson)
    infos = decodejson['result']
    # print(infos)
    # 获取想要的信息
    try:
        uid = infos['uid']
    except:
        uid = None
    # print(uid)
    try:
        street_id = infos['street_id']
    except:
        street_id = None
    # print(street_id)
    try:
        name = infos['name']
    except:
        name = None
    # print(name)
    try:
        address = infos['address']
    except:
        address = None
    # print(address)
    try:
        shop_hours = infos['detail_info']['shop_hours']
    except:
        shop_hours = None
    # print(shop_hours)
    try:
        detail_url = infos['detail_info']['detail_url']
    except:
        detail_url = None
    # print(detail_url)
    try:
        content_tag = infos['detail_info']['content_tag']
    except:
        content_tag = None
    # print(uid,street_id,name,address,shop_hours,detail_url,content_tag)
    Sql.insert_park(uid,street_id,name,address,shop_hours,detail_url,content_tag)