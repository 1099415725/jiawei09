# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/25   10:52
# 文件名称： other_databases.py
# 开发工具： PyCharm
import  pymysql

db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="1234", database="sys", charset="utf8")
cursor = db.cursor()

sql = '''
               create table mems(
                   id int primary key auto_increment,
                   name varchar(20) not null,
                   age int not null,
                   sex varchar (4)default "man",
                   tel int(11)
               )

           '''
cursor.execute(sql)

db.close()