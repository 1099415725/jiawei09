# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/16   8:44
# 开发工具： PyCharm

list1=[1,1]
list2=[]
while len(list2)<30:
    num1=list1[-1]+list1[-2]
    list1.append(num1)
    num2=list1[-1]/list1[-2]
    list2.append(num2)
num3=sum(list2[0:20])
print(list2)
print(num3)