'''
https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&=0&at=c7b50c7371c840b2ac125bbe252a7274&rt=3cb977cb951a4da283feb6ed3296e144&_v=0.71956504&userCode=665266014&x-zp-page-request- id=4f3a8bc8677348918ced853037b08408-1551179977119-732860
https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&=0&at=c7b50c7371c840b2ac125bbe252a7274&rt=3cb977cb951a4da283feb6ed3296e144&_v=0.71956504&userCode=665266014&x-zp-page-request-          id=4f3a8bc8677348918ced853037b08408-1551179977119-732860
https://fe-api.zhaopin.com/c/i/sou?start=270&pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&=0&at=c7b50c7371c840b2ac125bbe252a7274&rt=3cb977cb951a4da283feb6ed3296e144&_v=0.71956504&userCode=665266014&x-zp-page-request-id=4f3a8bc8677348918ced853037b08408-1551179977119-732860

https://fe-api.zhaopin.com/c/i/sou?start=270&cityId=530&kw=python

'''
'''
import requests
import os
import json

class siper(object):
    def __init__(self):
        self.header={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Origin":"https://sou.zhaopin.com",
            "Host":"fe-api.zhaopin.com",
            "Accept-Encoding":"gzip, deflate, br"
        }
        print("职位查询程序开始······")
        # 打开文件
        self.file = "result.json"
        path = os.getcwd()
        pathfile = os.path.join(path,self.file)
        self.fp = open(pathfile,"w",encoding="utf-8")
        self.fp.write("\n")

    def get_response(self,url):
        return requests.get(url=url,headers = self.header)

    def get_citycode(self,city):
        url = "https://fe-api.zhaopin.com/c/i/city-page/user-city?ipCity={}".format(city)
        response = self.get_response(url)
        result = json.loads(response.text)
        return result['data']['code']

    def parse_data(self,url):
        response = self.get_response(url)
        result = json.loads(response.text)['data']['results']
        items = []
        for i in result:
            item = {}
            item['职位'] = i['jobName']
            item['工资'] = i['salary']
            item['招聘状态'] = i['timeState']
            item['经验要求'] = i['workingExp']['name']
            item['学历要求'] = i['eduLevel']['name']
            items.append(item)
        return items

    def save_data(self,items):
        num = 0
        for i in items:
            num = num + 1
            self.fp.write(json.dumps(i,ensure_ascii=False))
            if num == len(items):
                self.fp.write("\n")
            else:
                self.fp.write(",\n")
            print("%s--%s"%(str(num),str(i)))

    def end(self):
        self.fp.write("]")
        self.fp.close()
        print("职位查询程序结束······")
        print("数据已写入到{}文件中······".format(self.file))

    def main(self):
        try:
            cityname = input("请输入你要查询的城市的名称（市级城市）：")
            city = self.get_citycode(cityname)
            url = "https://fe-api.zhaopin.com/c/i/sou?pageSize=200&cityId={}&workExperience=-1&education=5&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3".format(
                city)
            items = self.parse_data(url)
            self.save_data(items)
            self.end()
        except Exception as e:
            print("城市输入错误！！！（强制退出程序）")
            print(e)
            exit(0)


if __name__ == '__main__':
    siper = siper()
    siper.main()

'''

import os
import requests
import json
import time

class zhilianspider(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Origin": "https://sou.zhaopin.com",
            "Host": "fe-api.zhaopin.com",
            "Accept-Encoding": "gzip, deflate, br"
        }
        print('程序开始，下载中～～～')
        self.file = 'zhilian.json'
        path = os.getcwd() + '/'
        # print(path)
        pathfile = os.path.join(path,self.file)
        # print(pathfile)
        self.fp = open(pathfile,'a',encoding='utf-8')
        self.fp.write("\n")

    def get_url(self,page_num,type_nr):
        list = [x*90 for x in range(page_num)]
        for x in list:
            # 爬虫
            url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=653&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={}&kt=3&=0&at=c7b50c7371c840b2ac125bbe252a7274&rt=3cb977cb951a4da283feb6ed3296e144&_v=0.71956504&userCode=665266014&x-zp-page-request- id=4f3a8bc8677348918ced853037b08408-1551179977119-732860'.format(x,type_nr)
            html = requests.get(url=url,headers=self.headers)
            self.parse_url(html)


    def parse_url(self,html):
        # print(html.text)
        results = json.loads(html.text)['data']['results']
        # print(results)
        items = []
        for each in results:
            item = {}
            if len(each["updateDate"].replace('2019-','').split(' ')[0])<6:
                if ('1' in each["workingExp"]["name"] or '不限' in each["workingExp"]["name"]) and '10' not in each["workingExp"]["name"]:
                    # item["地点"] = each["city"]["display"]
                    item["发布时间"] = each["updateDate"].replace('2019-','').split(' ')[0]

                    item["工作名称"] = each["jobName"]
                    item["工作经验"] = each["workingExp"]["name"]
                    item["薪水"] = each["salary"]
                    item["待遇"] = each["jobTag"]["searchTag"]

                    item["公司名称"] = each["company"]["name"]
                    item["公司性质"] = each["company"]["type"]["name"]
                    item["公司大小"] = each["company"]["size"]["name"]
                    item["网址"] = each["positionURL"] + "l"

                    item["公司网址"] = each["company"]["url"] + "l"
                    item["回复率"] = each["rate"]
                    items.append(item)
            else:
                continue
            # print(item)
        time.sleep(1)
        self.download(items)

    def download(self,items):
        num = 0
        for i in items:
            num = num + 1
            self.fp.write(json.dumps(i,ensure_ascii=False))
            if num == len(items):
                self.fp.write("\n")
            else:
                self.fp.write(",\n")
            print("%s--%s"%(str(num),str(i)))


        print("数据已写入到{}文件中······".format(self.file))


    def main(self):
        page_num = input('请输入下载多少页:')
        type_nr = input('请输入查询内容：')
        if not page_num.isdigit():
            print('输入有误，请输入数字')
        else:
            page_num = int(page_num)
            self.get_url(page_num,type_nr)




if __name__ == '__main__':

    zl = zhilianspider()
    zl.main()



