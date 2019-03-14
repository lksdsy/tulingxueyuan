import pymongo


class MongoAPI(object):

    # 初始化变量及连接
    def __init__(self,db_ip,db_port,db_name,table_name):
        self.db_ip = db_ip
        self.db_port = db_port
        self.db_name = db_name
        self.table_name = table_name
        self.conn = pymongo.MongoClient('mongodb://root:ddd123@{}:{}'.format(self.db_ip,self.db_port))
        # 我mongodb设置了账号密码，　　　　　　　账号　　密码
        self.db = self.conn[self.db_name]
        self.table = self.db[self.table_name]


    # 获取数据
    def get_one(self,query):
        return self.table.find_one(query,property={"id":False})

    # 获取多条数据
    def get_all(self,query):
        return self.table.find(query)

    # 添加数据
    def add(self,kv_dict):
        return self.table.insert(kv_dict)

    # 删除数据
    def delete(self,query):
        return self.table.delete_many(query)

    # 查看集合中是否包含满足条件的数据，若有返回Ｔrue,否则则创建
    def check(self,query):
        ret = self.table.find_one(query)
        return ret != None
    def urdata(self,query,kv_dict):
        self.table.updata_one(query,{'$set':kv_dict},upsert=True)
