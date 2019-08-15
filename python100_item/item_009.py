# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/23   8:55
# 文件名称： item_009.py
# 开发工具： PyCharm

# 打印九九乘法表

for i in range(1,10):
    print('')
    for j in range (1,i+1):
        print("%d*%d=%d"%(i,j,i*j),end=" ")
print(" ")
