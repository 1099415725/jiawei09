# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/26   12:23
# 开发工具： PyCharm

import pymysql
# db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="1234", database="user_contact",
#                          charset="utf8")
# cursor = db.cursor()

class UserContact:
    db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="1234", database="user_contact",
                         charset="utf8")
    cursor = db.cursor()
    # @classmethod
    def add_user(self,name,sex,tel,note,email):
        # db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="1234", database="user_contact",
        #                      charset="utf8")
        # cursor = db.cursor()
        sql = "insert into user values(null,'%s','%s','%d','%s','%s')"%(name,sex,tel,note,email)

        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        self.cursor.close()
        self.db.close()

    @classmethod
    def add_contact(cls,c_name,c_sex,c_tel,c_email,c_channel,c_state,c_attachment,c_note,c_u_id):
        db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="1234", database="user_contact",
                             charset="utf8")
        cursor = db.cursor()
        sql = "insert into contact(id,name,sex,tel,email,channel,state,attachment,note,u_id)" \
              " values (null,'%s','%s','%d','%s','%s','%s','%s','%s','%d')"\
              %(c_name,c_sex,c_tel,c_email,c_channel,c_state,c_attachment,c_note,c_u_id)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        cursor.close()
        db.close()

    @classmethod
    def selt_contact(cls):
        db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="1234", database="user_contact",
                             charset="utf8")
        cursor = db.cursor()
        sql = "select u.name,u.tel,u.email,c.name,c.tel,c.email,c.sex,c.note from user u inner join contact c on u.id=c.u_id;"
        cursor.execute(sql)
        data = cursor.fetchall()
        print("u_name u_tel u_email c_name c_tel c_email c_sex c_note")
        for i in data:
            u_name = i[0]
            u_tel = i[1]
            u_email = i[2]
            c_name = i[3]
            c_tel = i[4]
            c_email = i[5]
            c_sex = i[6]
            c_note = i[7]
            print(u_name, u_tel, u_email, c_name, c_tel, c_email, c_sex, c_note)
        db.close()

    def tets(self):
        self.aaaa="123"


if __name__=="__main__":
    user = UserContact()
    user.tets()


    print(user.aaaa)