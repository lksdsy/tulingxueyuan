'''
酷狗top500抓取

url = 'http://www.kugou.com/yy/rank/home/1-8888.html?from=rank'
编号:1-23  共500条
最终数据存入mongodb
'''

import requests
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient

client = MongoClient('mongodb://root:ddd123@10.0.2.15:27017')
songs = client.KG_DB.songs

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

def kg_spider(url):
    rsp = requests.get(url,headers=headers)
    # print(rsp.text)
    soup = BeautifulSoup(rsp.text,'lxml')

    nums = soup.select('.pc_temp_num')
    # print(num)
    titles = soup.select('.pc_temp_songlist  > ul > li > a')
    # print(titles)
    times = soup.select('.pc_temp_time')
    # print(times)
    for num,title,time in zip(nums,titles,times):
        data = {
        # 歌曲编号
        'num':num.get_text().strip(),
        # print(num)
        # 歌曲名称
        'song':title.get_text().split('-')[-1].strip(),
        # print(song)
        # 歌手
        'singer':title.get_text().split('-')[0].strip(),
        # print(singer)
        # 歌曲时长
        'time':time.get_text().strip()
        # print(num,song,singer,song_time)
        }
        songs_id = songs.insert(data)
        print(songs_id)

if __name__ == '__main__':

    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1,24)]
    for url in urls:
        data = kg_spider(url)
        time.sleep(1)