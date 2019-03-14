'''
Ajax异步加载


https://www.pexels.com/?page=2
https://www.pexels.com/?page=3
https://www.pexels.com/?page=4

'''

import requests,re,time
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19'
}

photos = []

urls = ['https://www.pexels.com/?page={}'.format(str(i)) for i in range(1,10)]
# print(urls)
for url in urls:
    rsp = requests.get(url, headers=headers)
    # print(rsp.text)
    soup = BeautifulSoup(rsp.text,'lxml')
    imgs = soup.select('article > a > img')
    # print(imgs)
    # print(len(imgs))
    for img in imgs:
        photo = img.get('src')
        # print(photo)
        if photo.endswith('350'):
            photos.append(photo)
            # print(photo)

path = '/home/tlxy/tulingxueyuan/xuexi/data_type/img_Ajax'

for item in photos:
    data = requests.get(item,headers=headers)
    time.sleep(1)
    photo_name = re.findall('\d+\/(.*?)\?',item)
    # print(photo_name[0])
    if photo_name:
        fp = open(path+"/"+photo_name[0],"wb")
        fp.write(data.content)
        fp.close()
        print('下载完成'+photo_name[0])