# encoding ：UTF-8
# 开发团队：  DanceFlower
# 开发人员： 张伟
# 开发时间： 2019/7/16   22:41
# 文件名称： tice_716.py
# 开发工具： PyCharm

import  re
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
# dict={}
# dict[tel]=mem
# print(dict)
# ser_tel=input("请输入要查找的联系人电话:\n")
# for key in dict.keys():
#     if ser_tel==key:
#         val=dict[key]
#         print(val,  ser_tel)
#
# del_mem=input("请输入要删除的联系人：\n")

class Computer():
    '''
    cup;i7
    主板：华硕
    显卡;七彩虹
    内存：金士顿
    电源：海盗船
    机箱：牧马人
    '''
    def play_game(self):
        print("welcome to the league of dragon!")


xiaoming=Computer()
print(xiaoming)

xiaoming.play_game()

class Person():
    '''
    height;177
    weight:66kg
    home:hubei
    tel:13419591290

    '''
    def eat(self):
        print("i can eat!")

    @classmethod
    def study(self):
        print("i can study!")

    def play(self):
        print("i can play!")

    def cook(self):
        print("i can cook!")


liudehua=Person()
liudehua.cook()
liudehua.play()
liudehua.study()

class Ref:
    '''
    height:2.0m
    width:0,7m
    colour:red
    '''
    colour='green'



    def __init__(self,colour):
        print("aa")
        print("你是%s的垃圾"%colour)

    def open_door(self):
        '''
        来自远古的猛犸象
        :return:
        '''
        print("芝麻开门")
    def init_things(self,something):
        print("听说哟人要将%s装进冰箱"%something)

    def close_door(self):
        print("芝麻关门")

class Elephant:
    '''
    '''
    # 静态方法
    @staticmethod
    def play():
        print("来呀一起玩啊！")
    # 类方法
    @classmethod
    def walk(cls):
        print("我可以远征,带我去打仗！")
    # 实例方法
    def eat(self):
        print("我是一个肉食动物")
        self.play()


ref=Ref("red")

ele=Elephant()
ele.eat()

ele2=Elephant()
ele2.eat()

# ref.init_things(ele)
# Elephant.play()
# Elephant().play()
# Elephant.walk()
# Elephant().walk()
