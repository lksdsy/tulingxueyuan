# scrapy框架学习
    - 框架
    - 使爬虫变得相当简单
    - 异步网络框架Twistde(默认自带多线程)
    - 提供各种接口以及中间件
    
    
## scrapy长什么样子
    - Spider  爬虫
        - 1. 初次发起我们的爬虫请求
        - 2. 解析response得到的数据,若是url地址,则将其传递给调度器进行魂环爬取,若是数据,则将其传递给item,pipline
    - Scheduler 调度器
        - 负责接收引擎发送过来的requests请求,在此处进行队列的整合
    - downloader  下载器
        - 主要负责从互联网进行网页内容的请求
    - Item Pipline  数据存储
        - 主要负责spider中得到的数据(item),进行数据的处理与保存
    - Scrapy Engine  引擎
        - 负责spider item\pipline,scheduler,download之间的协调与通信/数据传递
    - Download Middlewares:
        - 下载中间件, 主要进行下载功能的扩展
    - Spider Middlewares:
        - 主要进行扩展spider功能/扩展与引擎之间的通信功能 
    

## scrapy框架的安装
    - 搭建虚拟环境
        - 查看所有的虚拟环境
            - conda env list  
        - 创建虚拟环境
            - conda create -n spider python=3.6
        - 激活虚拟环境
            - Linux:  source activate your_env_name(虚拟环境名称)

            - Windows: activate your_env_name(虚拟环境名称)
        - 安装scrapy
            - pip install scrapy
            
            
            
## 创建第一个scrapy项目
    - 创建项目
        - scrapy startproject projectName
    - 创建爬虫实例
        - scrapy genspider BaiduSpider baidu.com
            - BaiduSpider   爬虫名字
            - baidu.com     爬虫域名
            - 注意爬虫名字不能和项目名一样,否则报错
            
        