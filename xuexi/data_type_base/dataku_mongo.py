'''
mongodb属于更加适合爬虫的数据库
mongodb是一个基于分布式文件存储的数据库，由C++编写
主要为web应用提供可扩展的高性能数据存储解决方案


概念说明：
SQL         MongoDB        说明
database    database       数据库
table       collection     表/集合
row         document       行/文档
colume      field          字段/域
index       index          索引
primary     paimary        主键/_id为主键

'''

"""

# 查询mongodb


# 导入pymongo
import pymongo

# 连接mongodb数据库
# client = pymongo.MongoClient()
# client = pymongo.MongoClient('10.0.2.15', 27017) #常用
# client = pymongo.MongoClient('mongodb://10.0.2.15:27017')


#连接mydb数据库,账号密码认证
client = pymongo.MongoClient('mongodb://root:ddd123@10.0.2.15:27017')


# # 获取到数据库，连接数据库
db = client["xuexi"]


# 获取集合
std = db.dept

# 获取数据
datas = std.find()
# print(datas,type(datas))
for data in datas:
    # print(data['rank'])
    # 获取结合中的字段属性
    print(data.keys())
"""


# 插入文档

import pymongo

client = pymongo.MongoClient('mongodb://root:ddd123@10.0.2.15:27017')

# 创建数据库
db = client.lx

# 写入数据
post = {
    'name':'sy',
    'sex':'m',
    'age':'18',
    'class':['database','python','web','spider'],
    'income':'secret'
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print('post id is',post_id)

