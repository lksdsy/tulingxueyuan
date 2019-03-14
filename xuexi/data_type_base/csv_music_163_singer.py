'''
网易云音乐歌手信息抓取
url = "https://music.163.com/discover/artist/cat?id=1003&initial=67"

id=1003

id = [1/2/4/6/7/001,2,3]
initial=67
init = [-1,0,65-90]

'''

import requests,csv
from bs4 import BeautifulSoup

def get_artists(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Host':'music.163.com',
        'Referer':'https://music.163.com/'
    }

    req = requests.get(url,headers=headers)
    soup = BeautifulSoup(req.text,'lxml')
    for item in soup.find_all('a',attrs={'class':'nm nm-icn f-thide s-fc0'}):
        artist_name = item.string.strip()
        artist_id = item['href'].replace('/artist?id=','').strip()
        print(artist_id,artist_name,'成功')
        try:
            writer.writerow((artist_id,artist_name))
        except Exception as e:
            print('失败')
            print(e)


if __name__ == '__main__':

    id_list = [1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003, 4001, 4002, 4003]
    init_list = [-1, 0, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
                 89, 90]

    # 写入csv
    csvfile = open('music_163_artist.csv','a')
    writer = csv.writer(csvfile)
    writer.writerow(('artist_id','artist_name'))

    for i in id_list:
        for j in init_list:
            url = 'https://music.163.com/discover/artist/cat?id={}&initial={}'.format(i,j)
            # print(url)
            get_artists(url)
