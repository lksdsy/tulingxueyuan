import requests

class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv31.0) Gecko/20100101 Firefow/31.0'
        }

        res = requests.get(url,headers=headers)

        if res.status_code == 200:
            res.encoding = 'utf-8'
            return res.text
        return None