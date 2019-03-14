import requests
from lxml import etree
import csv
import re

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

rsp = requests.get('http://www.seputu.com/', headers=headers)

html = etree.HTML(rsp.text)

div_mulus = html.xpath('//*[@class="mulu"]')

rows = []
for div_mulu in div_mulus:
    div_h2 = div_mulu.xpath('.//div[@class="mulu-title"]/center/h2/text()')
    # print(h2_div)
    if len(div_h2) > 0:
        h2_title = div_h2[0]
        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            # 找href,title
            href = a.xpath('./@href')[0]
            box_title = a.xpath('./@title')[0]
            # print(href, box_title, type(box_title))

            pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
            match = pattern.search(box_title)
            if match != None:
                date = match.group(1)
                real_title = match.group(2)
                content = (h2_title, real_title, href, date)
                # print(content)
                rows.append(content)

headers = ['title', 'real_title', 'href', 'date']

with open('gcd.csv', 'a') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerow(rows)


