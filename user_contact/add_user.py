# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/26   9:58
# 文件名称： add_user.py
# 开发工具： PyCharm

import pymysql
# 向user 添加员工
db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="1234", database="user_contact", charset="utf8")
cursor = db.cursor()
sql = "insert into user values(null,'tom','man',50003,null,null)," \
      "(null,'jary','man',50004,null,null)," \
      "(null,'jack','man',50005,null,null)"
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print (e)
    db.rollback()
cursor.close()
db.close()