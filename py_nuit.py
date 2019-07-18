# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/11   12:30
# 文件名称： py_nuit.py
# 开发工具： PyCharm

# name=input("请输入你的大名：")
# print("你的大名叫："+name)
# print("你的大名叫：",name)
# print("你的大名叫：%s"%name)
# print(hex(ord('%')))
#
# born=int(input('输入你的出生年份：'))
# year=int(input('今年是哪一年：'))
# cc=year-born
# print (cc)
# print(int(year)-int(born))

# a=[2,4,5,3,1,9,6]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# print(sorted(a,reversed=True))
# a=-2
# print(type(a))
# a=3**4
# print (a)

#
# num1=input("输入一个数字：\n")
# num2=input("输入一个数字：\n")
#
# if num1<num2:
#     num3=num1
#     num1=num2
#     num2=num3
#     print(num1)
#     print (num2)


# 冒泡排序
list1=[18,16,15,13,12,11,6,4,2,1]
length=len(list1)
for i in range(1,length):
    print("coco")
    for j in range(1,length-i+1):
        if list1[j-1]>list1[j]:
            mem=list1[j-1]
            list1[j-1]=list1[j]
            list1[j]=mem
            print(list1)
print(list1)

code_list=['a','d','r','e','p','d','p','e','r','e']

popo="bshasbfdjkdsfjajdshfjnjvknaskhefnvckasdfaudsg"
# symble= str.count(sub , start, end)
# str要检索的字符串，
# sub要检索的子字符串
# start

unit=popo.count("a",3,15)
print(unit)

c=2019
d=11.03
e=15
coco=(c,d,e)
stg="%s/%05fd/%s"
print(stg%(c,d,e))

#编号：000000077	公司名称：百度 	 官网：http://www.baidu.com

