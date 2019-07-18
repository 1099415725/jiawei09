# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/16   9:55
# 文件名称： item_001.py
# 开发工具： PyCharm

# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
num=[1,2,3,4]
num2=[]
for i in num:
    for j in num:
        for k in num:
            if i!=j and j!=k and i!=k:
                num1 = i * 100 + j * 10 + k
                num2.append(num1)
print(num2)
print(len(num2))