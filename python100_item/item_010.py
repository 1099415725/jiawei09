# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/23   11:45
# 文件名称： item_010.py
# 开发工具： PyCharm


# 暂停五秒，并格式化当前日期
import  time

print (time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime(time.time())))

time.sleep(5)

print (time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime(time.time())))