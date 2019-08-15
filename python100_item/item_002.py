# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/16   10:03
# 文件名称： item_002.py
# 开发工具： PyCharm
'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
'''
profit=input("输入利润(万元)：\n")
try:
    float(profit)
except:
    print("请输入合法的利润！")

if profit<0:
    print("利润不能为负数")
elif profit<=10:
    bonus=profit*0.1
    print("奖金为：%.3f万元"%bonus)
elif profit<=20:
    bonus=1+(profit-10)*0.075
    print("奖金为：%.3f万元" % bonus)
elif profit<=40:
    bonus=1.75+(profit-20)*0.05
    print("奖金为：%.3f万元" % bonus)
elif profit<=60:
    bonus=2.75+(profit-40)*0.03
    print("奖金为：%.3f万元" % bonus)
elif profit<=100:
    bonus=3.35+(profit-60)*0.015
    print("奖金为：%.3f万元" % bonus)
elif profit>100:
    bonus=3.95+(profit-100)*0.01
    print("奖金为：%.3f万元" % bonus)
