数据库

1. 分类
    - 关系型数据库
        可视为excel表格
        Mysql
        DB2
        
    - 非关系型数据库
        MongoDB
        Redis
        Neo4j
2. 数据库指令
    - 操作不区分大小写（密码，变量值除外）
    - 每条SQL指令以  ;  结束或分割
    - 不支持Tab键自动补齐
    - \c 可废弃当前编写错的操作指令
    
3. 登录
    - mysql -u root -p
    - mysql[-h 服务器名 -u 用户名 -p 密码 数据库]
   
4. 操作
    - 退出    quit或exit
    - 查看数据库,列出当前Mysql服务器上有哪些数据库    show databases;
    - 使用/切换到指定数据库   use 数据库名 ;
    - 列出当前库所有的表     show tables;
    - 查看指定表的字段结构
        - describe 表名;     可以缩写为desc 表名;          
        - describe 表名\G;   表示以列形式查看
    - 查看当前所在数据库     select database(); 
  
5. 数据库命名
    - 可以使用数字/字母/下划线，但不能纯数字
    - 区分大小写，具有唯一性
    - 不可以使用关键字/特殊字符
    
6. 创建/删除数据库
    - 创建　　 create database 数据库名;
    - 删除    drop database 数据库名;

7. 新建/删除表
    - 新建create table 表名(
        字段1 字表类型(宽度) 约束条件,
        .................
        primary key (主键名)
        );
    - 删除drop table 表名;
    
8. 数据类型
    - 关于数值的说明
        - 使用unsigned修饰时，对应的字段只保存正数
        - 数值不够指定宽度时，在左边填空格补位
        - 宽度仅是显示宽度，存数值的大小由类型决定
        - 使用关键字zerofill时，填0代替空格补位
        - 当字段值与类型不匹配时，字段值作为0处理
        - 数值超出范围时，仅保存最大/最小值
    
    - 数值类型
        - tinyint: 1byte, -128-127, 0-255
        - smallint: 2byte, -32768-32767, 0-65535
        - mediumint: 3byte
        - int: 4byte,
        - bigint: 8byte,
        - float: float(m,d)
            - m: 总宽度
            - d: 小数位数
        - double 
        - decimal: ddecimal(m,d)
            - m: 有效位数
            - d: d小数位数
            - 占用m+2字节
          
    - 字符类型
        - char: 固定长度字符
            - 用法: char(n) ,n是长度
            - 最大长度255字符
            - 不够指定字符数时在右边用空格补齐
            - 自动阶段超出指定字符数的数据
        - varchar: 可变长字符
            - 用法: varchar(n) ,n是长度
            - 按数据实际大小分配存储空间
            - 自动截断超出指定字符数的数据
        - text/blob: 大文本类型
            - 字符数大于65535存储时使用
                