# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/24   19:20
# 文件名称： py_choose.py
# 开发工具： PyCharm
from py_mysql.pymsq import DoMems
while True:
    choice=input("选择你要进行的操作：\n1:增加学生信息\n2:删除学生信息\n3:修改学生信息\n4:查询学生信息\n按Q退出操作\n")
    if choice=="1":
        name=input("请输入学生姓名：")
        age=int(input("输入学生年龄："))
        sex=input("输入学生性别：")
        tel=int(input("输入学生电话："))
        stu=DoMems.ins_msg(name,age,sex,tel)

    elif choice=="2":
        tel1=int(input("输入删除学生的电话："))
        stu=DoMems.del_msg(tel1)
    elif choice=="3":
        name1=input("输入你要修改的学生姓名：")
        age1=int(input("输入修改后的学生年龄："))
        sex=input("输入修改后的而学生性别：")
        tel1=int(input("输入修改后的学生电话："))
        stu=DoMems.chg_msg(age1,tel1,sex,name1)
    elif choice=="4":
        name1=input("输入你要查询的学生姓名：")
        stu=DoMems.sel_msg(name1)
    elif choice=="Q":
        break