# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/25   8:56
# 文件名称： item_101.py
# 开发工具： PyCharm

# 1到n中1的个数
num=int(input("输入要查询的数字：\n"))
num2=0
for i in range(0,num+1):
    num1=str(i).count("1")
    num2+=num1
print(num2)



