'''
python连接mysqldemo
1. 获取数据库
2. 获取记录
3. 添加记录
4. 修改记录
5. 删除记录
6. .................

'''

__author__ = '作者名'

import pymysql

class MysqlDemo(object):
    # 设置数据库的连接参数，默认编码类型:utf-8,参数为字符串
    def __init__(self,host,username,password,dbname):
        self.conn = pymysql.connect(host,username,password,dbname,charset='utf8')
        self.cursor = self.conn.cursor()

    # 获取数据. 此处传值为sql语句
    # 多条
    def get_all(self,sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results

        except Exception as e:
            print(e)
            return False
    # 单条
    def get_one(self,sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
            return results
        except Exception as e:
            print(e)
            return False

    # 插入数据,
    def insert(self,table_name,data):
        if len(data.keys()) == 1:
            sql = 'insert into {}({}) values'.format(table_name,data.keys[0]).replace("'",'') +'("{}")'.format(data.values()[0])
        else:
            sql = 'insert into {}{} values'.format(table_name,tuple(data.keys())).replace("'",'') +str('{}'.format(tuple(data.values())))

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            # 返回插入后的id
            return int(self.cursor.lastrowid)
        except Exception as e:
            self.conn.rollback()
            print(e)
            return False

    # 执行一条sql语句
    def query(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            # 返回插入后的id
            return int(self.cursor.lastrowid)
        except Exception as e:
            self.conn.rollback()
            print(e)
            return False



    # 更新数据  tablename data(字典)  条件-字符串
    def updata(self,table_name,data,restrcation_str):
        data_str = ''
        for item in data.items():
            data_str +='{}="{}",'.format(item[0],item[1])
        values = data_str[:-1]
        sql = 'update {} set {} where {}'.format(table_name,values,restrcation_str)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            self.conn.rollback()
            print(e)
            return False


    # 删除一条记录 table_name restrcation_str

    # 删除表
    
    # 格式化表
    def format_tab(self,table_name):
        sql = 'trncate table table_name'
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            self.conn.rollback()
            print(e)
            return False