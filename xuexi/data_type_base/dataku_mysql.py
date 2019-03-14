'''
数据存储之mysql
Ubuntu环境安装mysql
    sudo apt-get update
    sudo apt-get install mysql-server
    sudo apt-get install mysql-client
    sudo apt-get install libmyqslclient-dev

登录数据库：
    sudo mysql -u root -p

rhel7环境安装mysql数据可
    https://www.cnblogs.com/guozhiping/p/7684134.html

mysql数据库远程连通：
    1. 修改/etc/mysql/my.conf
        找到bind-address = 127.0.0.1这一行，将其注释
        或者将其改为bind-address = 0.0.0.0

    2.让root用户支持远程连接mysql数据库
        mysql -u root -p
        grant all privileges on *.* to root@'%' identified by "设置的密码" with grant option;
        flush privileges
    3. rhel7中防火墙允许mysql服务通过
        firewall-cmd -- permanent --add-service=mysql
        firewall-cmd --reload

Python操作mysql(pymysql)
    pip install pymysql

'''
# 10.0.2.15
# Python3操作mysql创建数据表


import pymysql

# 创建一个表
# try:
#     # 获取数据库连接,注意：若是utf-8类型，需要定制数据库
#     # 打开数据库连接
#     db = pymysql.connect(host='10.0.2.15', user='root', passwd='ddd123', db='xuexi', port=3306)
#     '''
#     host = '10.0.2.15',     数据库服务器地址
#     user = 'root',          登录用户数据库用户
#     passwd = 'ddd123',      用户密码
#     db = 'xuexi',           所连接的数据库名
#     port = 3306             数据库端口号,mysql默认3306
#     '''
#     # print(db)
#     # 创建游标，对数据进行操作，使用cursor()方法
#     cursor = db.cursor()
#     # 使用execute()执行sql语句
#     cursor.execute('DROP TABLES IF EXISTS LX')
#     # 使用预处理语句创建表
#     sql = """create table LX(
#     FIRST_NAME CHAR(20) NOT NULL,
#     LAST_NAME CHAR(20),
#     AGE INT,
#     SEX CHAR(1),
#     INCOME FLOAT)"""
#     cursor.execute(sql)
#     db.close()
# except:
#     print('创建失败')




# # 数据库插入操作
#
# db = pymysql.connect('10.0.2.15', 'root', 'ddd123', 'xuexi')
#
# #利用cursor()创建游标对象
# cursor = db.cursor()
#
# # sql 插入语句
# sql = 'insert into LX(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)VALUE("s1","y",18,"M","0"),("h","lb",28,"M","100000")'
#
# # 为了防止sql注入,可将其写为如下所示
# # sql = 'INSERT INTO LX(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)VALUES("%s","%s","%d","%c","%s")'%("s","y",18,"M","1110")
#
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提交执行
#     db.commit()
#     print('成功')
# except:
#     # 发生意外
#     db.rollback() # 回滚
#     print('失败')
# db.close()


# 数据库查询操作
# try:
#     db = pymysql.connect('10.0.2.15', 'root', 'ddd123', 'xuexi', 3306)
#     cursor = db.cursor()
#     cursor.execute('select * from LX')
#     # datas = cursor.fetchall()
#     # for data in datas:
#     #     print(data)
#     datas = cursor.fetchone()
#     for data in datas:
#         print(data)
#     cursor.close()
#     db.close()
# except:
#     pass

'''
数据库查询：
    fetchall()    接收全部返回结果
    fetchone()    获取下一个查询结果集
    rowcount()    只读属性，返回执行语句影响的行数
'''


# 数据库更新操作

# db = pymysql.connect('10.0.2.15', 'root', 'ddd123', 'xuexi')
# cursor = db.cursor()
#
# # sql 更新语句
# sql = "UPDATE LX SET AGE = AGE-1 WHERE FIRST_NAME='%s'"%('s1')
#
# try:
#     cursor.execute(sql)
#     db.commit()
#     print('成功')
# except:
#     db.rollback()
#     print('失败')
#
# db.close()




# 数据库删除操作
db = pymysql.connect('10.0.2.15', 'root', 'ddd123', 'xuexi')
cursor = db.cursor()

#　sql 删除语句
sql = "DELETE FROM LX WHERE INCOME < '%d'"%(100)

try:
    cursor.execute(sql)
    db.commit()
    print('成功')
except:
    db.rollback()
    print('失败')
db.close()

