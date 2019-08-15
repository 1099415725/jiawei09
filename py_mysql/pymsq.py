# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/24   15:13
# 文件名称： pymsq.py
# 开发工具： PyCharm

import pymysql


# def connectmysql():
#     db=pymysql.connect(host="127.0.0.1",port=3306,user="root",password="1234",database="employer",charset="utf8")
#
#     cursor=db.cursor()
#
#     cursor.execute("select * from employee;")
#
#     data = cursor.fetchone()
#
#     print(data)
#
#     db.close()
class DoMems():

    # 在数据库中建立表
    @classmethod
    def createtable(cls):
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

    #      插入数据
    @classmethod
    def ins_msg(cls, name, age, sex, tel):
        db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="1234", database="sys", charset="utf8")
        cursor = db.cursor()
        sql = "insert into mems values(null,'%s','%d','%s','%d')" % (name, age, sex, tel)
        try:
            cursor.execute(sql)
            # 向数据库提交
            db.commit()
        except Exception as e:
            print (e)
            # 发生错误时 回滚
            db.rollback()
        cursor.close()
        db.close()

    #     删除数据
    @classmethod
    def del_msg(cls, tel1):
        db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="1234", database="sys", charset="utf8")
        cursor = db.cursor()
        sql = "delete from mems where tel=%d" % (tel1)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.rollback()
        db.close()

    #    更改数据
    @classmethod
    def chg_msg(cls, age1, tel1, sex, name1):
        db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="1234", database="sys", charset="utf8")
        cursor = db.cursor()
        sql = "update mems set age ='%d',tel='%d' ,sex='%s' where name = '%s'" % (age1, tel1, sex, name1)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.rollback()

        db.close()

    #     查询
    @classmethod
    def sel_msg(cls, name1):
        db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="1234", database="sys", charset="utf8")
        cursor = db.cursor()
        sql = "select * from mems where name='%s'" % name1
        cursor.execute(sql)
        data = cursor.fetchall()
        for i in data:
            id = i[0]
            name = i[1]
            age = i[2]
            sex = i[3]
            tel = i[4]
            print(id, name, age, sex, tel)
        db.close()
