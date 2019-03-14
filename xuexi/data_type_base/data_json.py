'''
python对json文件操作分为编码和解码
编码:
    dump     json对象　　可以通过fp文件流写入文件
    dumps    字符串
解码:
    load     json
    loads    字符串
'''

# import json
#
# str1 = "[{'username':'haha', 'age':18}]"
# # print(type(str1))
#
# # 编码
# json_str = json.dumps(str1, ensure_ascii=False)
# print(json_str)
# print(type(json_str))
#
# # 解码
# new_str = json.loads(json_str)
# print(new_str, type(new_str))


import requests,json
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

rsp = requests.get('http://www.seputu.com/', headers=headers)

soup = BeautifulSoup(rsp.text,'lxml')

content = []
for mulu in soup.find_all(class_='mulu'):
    # 标题
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string  # 获取标题
        list1 = []
        # 获取章节标题和url地址
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            # print(href, box_title)
            list1.append({'href':href, 'box_title':box_title})
        content.append({'title':h2_title, 'content':list1})

with open('gcd.json', 'a', encoding='utf-8') as f:
    json.dump(content, fp=f, indent=4, ensure_ascii=False)
