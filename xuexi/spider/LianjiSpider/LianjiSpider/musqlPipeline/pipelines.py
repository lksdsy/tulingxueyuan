from .sql import Sql
from xici.items import XiciDailiItem
class XiciDailiPipeline():
    def process_item(self,item,spider):
        if isinstance(item,XiciDailiItem):
            ipaddress = item['ipaddress']
            ret = Sql.select_name(ipaddress)
            if ret[0] == 1:
                print("已经存在啦！")
                pass
            else:
                # country, ipaddress, port, serveraddr, isanonymous, type, alivetime, Verifictiontime
                country = item['country']
                ipaddress = item['ipaddress']
                port = item['port']
                serveraddr = item['serveraddr']
                isanonymous = item['isanonymous']
                type = item['type']
                alivetime = item['alivetime']
                Verifictiontime =  item['Verifictiontime']
                Sql.insert_db_xici(country, ipaddress, port, serveraddr, isanonymous, type, alivetime, Verifictiontime)
                print("………………………………")