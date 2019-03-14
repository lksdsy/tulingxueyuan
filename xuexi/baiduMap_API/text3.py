import requests
import json
from xuexi.baiduMap_API.MysqlAPI import Sql

city_list = []

with open('/home/tlxy/tulingxueyuan/xuexi/baiduMap_API/cities.txt','r',encoding='utf-8') as f:
    for eachline in f:
        # print(eachline)
        fileds = eachline.split('\t')
        # print(fileds)
        city = fileds[0]
        city_list.append(city)
        num = fileds[1].replace('\n','')


def getjson(loc,page_num=0):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    data = {
        'query':'公园',
        'region':loc,
        'scope':'2',
        'page_size':20,
        'page_num': page_num,
        'output':'json',
        'ak': 'gXaG3THhX2OO20c2T8eUMIHHe8X528GQ',
    }
    url = 'http://api.map.baidu.com/place/v2/search?'
    res = requests.get(url,params=data,headers=headers)
    decodejson = res.json()
    # print(res.url)

    return decodejson


for ect in city_list:
    flag = True
    page_num = 0
    while flag:
        decodejson = getjson(ect,page_num)
        # print(ect,page_num)
        if decodejson['results']:
            for eachone in decodejson['results']:
                # print(eachone)
                try:
                    park = eachone['name']
                except:
                    park = None
                try:
                    location_lat = eachone['location']['lat']
                except:
                    location_lat = None
                try:
                    location_lng = eachone['location']['lng']
                except:
                    location_lng = None
                try:
                    address = eachone['address']
                except:
                    address = None
                try:
                    street_id = eachone['street_id']
                except:
                    street_id = None
                try:
                    uid = eachone['uid']
                except:
                    uid = None

                # print(ect,park,location_lat,location_lng,address,street_id,uid)
                Sql.insert_city(ect,park,location_lat,location_lng,address,street_id,uid)
            page_num += 1
        else:
            flag = False
