# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/16   20:15
# 文件名称： tice_716.py
# 开发工具： PyCharm


# 任务一，字符串综合训练
# voice="2018 Amazon Jeff Bezos 1120"
# coco=voice[5:]
# print(coco)
# popo=voice.split()
# print(popo)
# result=popo[0]+popo[-1]
# print(result)
# coco1=voice[5:-5]
# result1="【"+popo[0]+"】"+coco1+"【"+popo[-1]+"】"
# print(result1)
# new_str=popo[0]+popo[1]+popo[2]+popo[3]+popo[-1]
# print(new_str)
# db_new_str=str(int(popo[0])*2)+popo[1]+popo[2]+popo[3]+str(int(popo[-1])*2)
# print(db_new_str)
# str_list="要么创新，要么杰夫.贝索斯会替你做"


# 任务2;查找字符串中字符出现的次数
# stg=input("请输入一串字符串：\n")
# stg1=input("请输入一个字符：\n")
# stg2=str(stg.count(stg1))
# print(stg1+"在字符串"+stg+"中出现的次数是："+stg2+"次")

# 任务3：格式化输出商品的编号和单价

num=("%s\t%s\t%s\t%s"%("商品号","商品名称","单位","单价"))
print(num)




# 任务4：删除字符串中重复的字符
# db_input=input("请输入一个字符串：\n")
# new_input=''
# for i in db_input:
#     if i not in new_input:
#         new_input+=i
# print(new_input)

# 任务5：输出身份证上的生日信息
# data=input("请输入你的身份证号码：\n")
# num1=data[6:10]
# num2=data[10:12]
# num3=data[12:14]
# num4=int((data[-1]))%2
# sex=[]
# if num4==1:
#     sex.append("女")
# else:
#     sex.append("男")
# print("%s年%s月%s日%s"%(num1,num2,num3,sex[0]))


# 字典任务2，手机通讯录管理
# 添加联系人
# mem=input("请输入联系人姓名：\n")
# tel=input("请输入联系人电话：\n")
# dict={'渣渣灰':'13312345678'}
# dict[mem]=tel
# print(dict)
# ser_tel=input("请输入要查找的联系人电话:\n")
# for member in dict.items():
#     if ser_tel==member[-1]:
#
#         print(member[0],member[-1])
#
# del_mem=input("请输入要删除的联系人：\n")
# for member in dict.items():
#     print(member)
#     if del_mem==member[0]:
#         print("确认要删除%s\t%s的联系人吗?"%(member[0],member[-1]))
#         print("输入1，删除联系人  2,取消，不删除\n")
#         clips=int(input("请输入你的选择："))
#         if clips==1:
#             print("联系人%s已删除" % member[0])
#             del dict[member[0]]
#             break



# 函数
# 任务1;计算精英黑客对讲机
# 定义一个方法，对输入的数字进行转义
# def sec_lag():
#     secret={"0":'O',"1":"I",'2':'Z','3':'E','4':'Y','5':'S','6':'G','7':'L','8':'B','9':'P'}
#     language=input("输入暗语：\n")
#     lang_dic=""
#     for item in language:
#         values1=secret[item]
#         lang_dic+=values1
#     print(lang_dic)
#
# sese=sec_lag()


# 任务2，货币币值兑换系统
#
# def chg_money():
#     print("1人民币=9.912俄罗斯卢布\n1俄罗斯卢布=0.1009人民币")
#     chg=input("选择你要进行的操作：1，人民币兑换卢布  2，卢布兑换人民币\n")
#     if chg=="1":
#         chg1=int(input("输入人民币金额:\n"))
#         chg_res=chg1*9.912
#         print("可以兑换%sRUB"%chg_res)
#     elif chg=="2":
#         chg2=int(input("输入卢布金额：\n"))
#         chg_res1=chg2*0.1009
#         print('可以兑换%sRMB'%chg_res1)
#
# money=chg_money()

# 任务3星座判断函数
def start():
    bir={"魔羯座":(101,119),"水瓶座":(120,218),"双鱼座":(219,320),"白羊座":(321,419),"金牛座":(420,520),"双子座":(521,621),"巨蟹座":(622,722),"狮子座":(723,822),"处女座":(823,922),"天秤座":(923,1023),"天蝎座":(1024,1122),"射手座":(1123,1220),"魔羯座":(1221,1231)}
    birthday=int(input("请输入你的生日(格式：xxxx):\n"))

    for date in bir.items():
        num=date[1]
        if num[0]<=birthday<=num[1]:
            print("你的星座是%s"%date[0])
        else:
            print("输入有误！")

coco=start()