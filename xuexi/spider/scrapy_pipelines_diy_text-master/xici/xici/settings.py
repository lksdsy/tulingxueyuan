# -*- coding: utf-8 -*-

# Scrapy settings for xici project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xici'

SPIDER_MODULES = ['xici.spiders']
NEWSPIDER_MODULE = 'xici.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xici (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
        "Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language":" zh-CN,zh;q=0.9",
        "Cache-Control":" max-age=0",
        "Connection":" keep-alive",
        "Cookie":" _free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTZkOTk1OTcwNjU4MDQwNGVkYjg2NGYxMmZmY2UyYmQ5BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMS9oc25BL1ZzdjBEalhyemZTbitjYVRvTlg5cExWSG53UUNRUzBsajJYUE09BjsARg%3D%3D--2568f58683b3ec574fc6d39d86602f6e86399c92; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1524014009,1524014045; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1524014045",
        "Host":" www.xicidaili.com",
        "If-None-Match":' W/"096659f7645840d2c00b426aa9022adb"',
        # "Referer":" https://www.baidu.com/link?url=JuAmxoxL6MmvbvDR6NnHc-1ncZjgrSe8GaFnfswwoJSlGxjRasYxRXua86_lH-A1&wd=&eqid=aac7950900045e32000000055ad69bb2",
        "Upgrade-Insecure-Requests":" 1",
        "User-Agent":" Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xici.middlewares.XiciSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'xici.middlewares.XiciDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'xici.pipelines.XiciPipeline': 300,
   'xici.mysqlpipelines.pipelines.XiciDailiPipeline':1,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


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




#定义mysql配置文件、
#定义mysql配置文件
MYSQL_HOSTS = '192.168.0.100'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'redhat'
MYSQL_PORT = 3306
MYSQL_DB = 'db_xici'