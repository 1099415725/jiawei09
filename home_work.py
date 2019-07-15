# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/11   18:01
# 文件名称： home_work.py
# 开发工具： PyCharm


weight = float(input("请输入你的体重（kg）："))
height = float(input("请输入你的升高(m)："))
BMI = weight / (height ** 2)
if BMI <= 18.5:
    print("魔鬼身材！")
elif 18.5 < BMI <= 24.5:
    print("体重正常，继续保持！")
elif 24.5 < BMI <= 28.0:
    print("小胖子，你得锻炼了！")
elif BMI > 28.0:
    print("你太胖了，少吃多运动！")
else:
    print("输入有误！")

money = input("请输入你的消费金额（元）：\n")
print("付款金额为:%s" % money + "\n""支付成功，对方已收款！")

print("我爱你一生一世！")
print(float(520.1314))
print(int(5201314))

attack = input("请输入攻击值：")
defense = input("请输入防御值：")
force = input("请输入武力值：")
command = input("请输入统率值：")
speed = input("请输入速度值：")
intelligence = input("请输入智力值;")
print("攻击 %s \n防御 %s\n武力 %s\n统率 %s\n速度 %s\n智力 %s" % (attack, defense, force, command, speed, intelligence))

choose1 = int(input("亚当你要出什么：\n1,石头\n2,剪刀\n3,布\n"))
choose2 = int(input("夏娃你要出什么：\n1,石头\n2,剪刀\n3,布\n"))
if choose1 == choose2:
    print("平局")
elif choose1 == 1 and choose2 == 2:
    print("亚当胜！")
elif choose1 == 1 and choose2 == 3:
    print('夏娃胜！')
elif choose1 == 2 and choose2 == 3:
    print("亚当胜！")
elif choose1 == 2 and choose2 == 1:
    print("夏娃胜！")
elif choose1 == 3 and choose2 == 2:
    print("夏娃胜！")
elif choose1 == 3 and choose2 == 1:
    print("亚当胜！")


# 20200110