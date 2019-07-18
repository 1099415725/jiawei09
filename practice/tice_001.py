# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/16   10:32
# 文件名称： tice_001.py
# 开发工具： PyCharm
import re
pattern=r"mr_\w+"
string="MR_SHOP mr_shop"
# re.I，匹配的时候是否区分大小写
# match()从开头开始匹配，如果开头无法匹配到，则会直接返回None
stg=re.match(pattern,string,re.I)
print(stg)
print(stg.start())
print(stg.end())
print(stg.span())
print(stg.string)
# search()从头开始匹配，会从头到尾一直匹配下去，只要和匹配的对象相同就会匹配到
stg=re.search(pattern,string)
print(stg)

stg=re.findall(pattern,string,re.I)
print(stg)

# 语法：
# 	re.sub(pattern, repl, string, count, flags)
tel=r"1[358]\d{9}"
str="联系电话是：13419591290"



list1=[1,2,3,4,5,]
list2=['a','b','c','d','e']
list=zip(list2,list1)
print(list)
print(type(list))
dictionary=dict(list)
print(dictionary)
idle=dictionary
# popitem随机移除字典中的值
# vv=idle.popitem()
# print(vv)
pop=idle["c"]
print(pop)
yuyu={'a':1 , 'e': 5, 'b': 2, 'c': 3, 'd': 4}
kafuka=yuyu['e'] if "e" in yuyu else "不存在"
print(kafuka)
tyty=yuyu.get("t",'popololo')
print(tyty)
for steps in yuyu.items():
    print (steps)

for apple,orange in yuyu.items():
    print(apple,":",orange)

for apple in yuyu.keys():
    print(apple)

for orange in yuyu.values():
    print(orange)

yuyu['m']='haha'
print(yuyu)

yuyu['a']='good'
print(yuyu)

del yuyu['c']
print(yuyu)


# 通过传入的身高和体重来计算BMI，判断身体状况
def fix_bmi(name,height,weight):
    '''
    通过传入的数据，计算身体的状况
    :param name:  姓名
    :param height: 身高  单位：米（m）
    :param weight: 体重  单位：千克（kg）
    :return: 返回的值
    '''

    bmi=weight/height**2
    if bmi<=18.5:
        print("魔鬼身材，去当模特吧！")
    elif bmi<=24.0:
        print("身材挺好的，前凸后翘！")
    elif bmi<=28.0:
        print("你的生菜不是一般的丰满")
    else:
        print('我有你洗澡的照片！')

fix_bmi("奥尼尔",2.15,200)


def what_school(chinese,match,english,all_since):
    '''
    计算成绩，看看是几等院校！
    :param chinese: 语文得分
    :param match:   数学得分
    :param english: 外语得分
    :param all_since: 综合考试得分
    :return:
    '''
    score=chinese+match+english+all_since
    if score>620.0:
        print("985院校已经为你敞开了大门！！")
    elif score>570.0:
        print("211院校欢迎你！")
    elif score>525.0:
        print("一类院校，你的最佳选择！")
    elif score>496.0:
        print("二本过了，")
    else:
        print("来呀，一起玩挖机呀！")
what_school(130,144,122,235)
# 定义一个方法，来计算长方形的面积
def font_size(height,width):
    '''
    根据闯入的参数，来激素那长方形的面积
    :param height: 长方形的高  单位:厘米（cm）
    :param width:  长方形的宽  单位：厘米（cm）
    :return:
    '''
    size_font=height*width
    print("长方形的面积为：%s平方厘米"%size_font)

font_size(20.0,23.5)

def cir_size(r):
    '''
    更具传入的半径来计算，圆的面积
    :param r: 圆的半径  单位：厘米（cm）
    '''
    size_font=3.14*(r**2)
    print("圆的面积是：%s平方厘米"%size_font)

cir_size(14)