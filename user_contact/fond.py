# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/26   11:05
# 文件名称： fond.py
# 开发工具： PyCharm

import pymysql

# 查询功能
db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="1234", database="user_contact", charset="utf8")
cursor = db.cursor()
sql = "select u.name,u.tel,u.email,c.name,c.tel,c.email,c.sex,c.note from user u inner join contact c on u.id=c.u_id;"
cursor.execute(sql)
data = cursor.fetchall()
print("u_name u_tel u_email c_name c_tel c_email c_sex c_note")
for i in data:
    u_name = i[0]
    u_tel= i[1]
    u_email= i[2]
    c_name= i[3]
    c_tel= i[4]
    c_email=i[5]
    c_sex=i[6]
    c_note=i[7]
    print(u_name,u_tel,u_email,c_name,c_tel,c_email,c_sex,c_note)
db.close()