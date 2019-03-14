# Scrapy Shell
    - 交互终端
    - python开发环境下
    - ipython

## 启动Scrapy Shell
    - scrapy shell 'www.baidu.com'
    - response.body.decode('utf-8')
    
## Scrapy 提供的选择器
    - 基本选择器
        - xpath(): 传入xpath表达式，得到selector list
        - extract(): 序列化读节点末unicode字符串列表
        - css(): 传入css表达式，返回selector list,语法规则同BeautifulSoup4
        - re(): 传入正则表达式进行规则

## 存储json
    - scrapy crawl name -o xxx.json        
## Scrapy日志等级
    - debug 调试信息(默认)
    - info 一般信息
    - waning 警告信息
    - error 一般错误
    - critical 严重错误
## Scrapy日志设置 在setting里填写
    - LOG_ENABLED 默认True，启用日志
    - LOG_ENCODING 编码类型，默认utf-8
    - LOG_FILE 日志的输出文件，默认当前路径下，可改
    - LOG_LEVEL 默认为debug

        