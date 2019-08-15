# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/26   10:21
# 文件名称： add_contact.py
# 开发工具： PyCharm

import pymysql
# 向contact 用户表中添加数据
db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="1234", database="user_contact", charset="utf8")
cursor = db.cursor()
sql = "insert into contact(id,name,sex,tel,u_id) values(800001,'吴彦祖','man',133123456,1001)," \
      "(800002,'刘德华','man',133123457,1001)," \
      "(800003,'张家辉','man',133123458,1002)," \
      "(800004,'张学友','man',133123459,1002)," \
      "(800005,'邓紫棋','woman',133123450,1003)," \
      "(800006,'景甜','woman',133123451,1003)," \
      "(800007,'高圆圆','woman',133123452,1004)"

try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print (e)
    db.rollback()
cursor.close()
db.close()