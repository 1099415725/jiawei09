# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/25   20:34
# 文件名称： practice.py
# 开发工具： PyCharm
import pymysql
db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="1234", database="class", charset="utf8")
cursor = db.cursor()
sql = "select * from student"
cursor.execute(sql)
data = cursor.fetchall()
for i in data:
    id = i[0]
    name = i[1]
    print("学号：%d\t姓名：%s"%(id,name))