# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/26   11:46
# 开发工具： PyCharm
from contact_user.body_sys import UserContact

while True:
    choice=input("选择操作：1，添加员工\n2,添加客户\n3,查询\nQ,退出操作\n")
    if choice=="1":
        name=input("员工姓名：")
        sex=input("员工性别：")
        tel=("员工电话：")
        note=("员工备注：")
        email=("员工邮箱：")
        user_add=UserContact.add_user(name,sex,tel,note,email)
    elif choice=="2":
        c_name=input("客户姓名：")
        c_sex=input("客户性别：")
        c_tel=int(input("客户电话："))
        c_email=input("客户邮箱：")
        c_channel=input("客户路径：")
        c_state=input("客户状态：")
        c_attachment=input("客户附件：")
        c_note=input("客户备注：")
        c_u_id=int(input("经办人编号："))
        contact_add=UserContact.add_contact(c_name,c_sex,c_tel,c_email,c_channel,c_state,c_attachment,c_note,c_u_id)

    elif choice=="3":
        s_contact=UserContact.selt_contact()

    elif choice=="Q":
        break
