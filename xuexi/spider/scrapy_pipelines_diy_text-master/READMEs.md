# scrapy_pipelines_diy_text
scrapy框架自定pipelines练习
本试验只要是利用scrapy爬去西祠代理数据来测试自定义pipeline


简要过程：
第一步：
	更改settings设置
	首先放开# Obey robots.txt rules   #曾经面试考官问怎么看待这个协议，四个字 “盗亦有道”
			ROBOTSTXT_OBEY = False
			
	可以设置相关request_headers
	
	DEFAULT_REQUEST_HEADERS = {
        "Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language":" zh-CN,zh;q=0.9",
        "Cache-Control":" max-age=0",
        "Connection":" keep-alive",
        		"Cookie":"_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTZkOTk1OTcwNjU4MDQwNGVkYjg2NGYxMmZmY2UyYmQ5BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMS9oc25BL1ZzdjBEalhyemZTbitjYVRvTlg5cExWSG53UUNRUzBsajJYUE09BjsARg%3D%3D--2568f58683b3ec574fc6d39d86602f6e86399c92; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1524014009,1524014045; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1524014045",
        "Host":" www.xicidaili.com",
        "If-None-Match":' W/"096659f7645840d2c00b426aa9022adb"',
        # "Referer":" https://www.baidu.com/link?url=JuAmxoxL6MmvbvDR6NnHc-1ncZjgrSe8GaFnfswwoJSlGxjRasYxRXua86_lH-A1&wd=&eqid=aac7950900045e32000000055ad69bb2",
        "Upgrade-Insecure-Requests":" 1",
        "User-Agent":" Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    }
	
	取消下面这些注释，可以调高效率，在缓存中查找
	
	HTTPCACHE_ENABLED = True
	HTTPCACHE_EXPIRATION_SECS = 0
	HTTPCACHE_DIR = 'httpcache'
	HTTPCACHE_IGNORE_HTTP_CODES = []
	HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
	
	日志管理
	#日志管理
	#日志文件
	LOG_FILE = 'sys.log'

	#日志等级
	LOG_LEVEL = 'ERROR'

	#是否启用日志
	LOG_ENABLED = True #启用日志

	#日志编码
	# LOG_ENCODING='utf-8'

	#如果是True,进程当中 所有标准输出（包括错误）将会被
	#重定向中到log中。例如，代码当中的print()
	LOG_STDOUT = False#(默认值为False)
	
	
第二步:
	创建Items(scrapy爬虫必要一步)
	
	class XiciDailiItem(scrapy.Item):
    country = scrapy.Field()
    ipaddress = scrapy.Field()
    port = scrapy.Field()
    serveraddr = scrapy.Field()
    isanonymous = scrapy.Field()
    type = scrapy.Field()
    alivetime = scrapy.Field()
    Verifictiontime = scrapy.Field()
	
第三步：
	创建爬虫，第一次手动创建直接创建xcdl.py文件，一直报错，后来用命令创建ok（scrapy genspider xcdl www.xcdl.com）
	
	爬虫完成后可以自行测试：
	scrapy crawl xcdl -o xici.json    可支持多个类型文件，常用如json,csv,xml等等
	
第四步;
	创建自定义mysqlpipelines，其中包括三个文件sql.py,pipelines.py,还有__init__.py
	三个文件内容请自行查看源码，作用此处不祥解
	
	在此之前设置mysql信息，可以在settings中设置也可以在sql中设置，此处在settings设置
	#定义mysql配置文件
		MYSQL_HOSTS = '192.168.0.100'
		MYSQL_USER = 'root'
		MYSQL_PASSWORD = 'redhat'
		MYSQL_PORT = 3306
		MYSQL_DB = 'db_xici'

第四步;
	完成pipelines的操作
	sql.py中存放sql语句
	pipelines中设置存储方式
	
	
最后发现写了一大丢bug，改！改！改………………OK！
代码为初级代码，若有疑问或者建议请致邮（yuxiang000@foxmail.com）谢谢！
	
