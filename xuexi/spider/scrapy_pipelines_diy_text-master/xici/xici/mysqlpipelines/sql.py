import pymysql
from xici import settings

MYSQL_HOST = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD =settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

db = pymysql.connect(user = MYSQL_USER,password = MYSQL_PASSWORD,host = MYSQL_HOST,port = MYSQL_PORT,database = MYSQL_DB,charset = "utf8")
cousor = db.cursor()
class Sql():
    @classmethod
    def insert_db_xici(cls,country,ipaddress,port,serveraddr,isanonymous,type,alivetime,Verifictiontime):
        sql = 'insert into xicidaili(country,ipaddress,port,serveraddr,isanonymous,type,alivetime,Verifictiontime) VALUES (%(country)s,%(ipaddress)s,%(port)s,%(serveraddr)s,%(isanonymous)s,%(isanonymous)s,%(alivetime)s,%(Verifictiontime)s)'
        # sql = 'insert into xicidaili(country,ipaddress,port,serveraddr,isanonymous,type,alivetime,Verifictiontime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'

        value = {
            "country":country,
            "ipaddress":ipaddress,
            "port":port,
            "serveraddr":serveraddr,
            "isanonymous":isanonymous,
            "type":type,
            "alivetime":alivetime,
            "Verifictiontime":Verifictiontime
        }
        try:
            cousor.execute(sql,value)
            db.commit()
        except Exception as e:
            print("出入失败",e)
            # cousor.rollback()


    #去重
    @classmethod
    def select_name(cls,ipaddress):
        sql = "select exists(select 1 from xicidaili where ipaddress=%(ipaddress)s)"
        value = {
            "ipaddress":ipaddress
        }

        cousor.execute(sql,value)
        return cousor.fetchall()[0]