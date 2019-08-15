# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/5   10:12
# 开发工具： PyCharm

from datetime import datetime
today = datetime.now().weekday()
import  csv
DATA=0
NAME=1
RECO_TYPE=5
RECO_TIME=6
RECO_STATUE=10

target_file = open("work_time.csv",encoding="utf8")
csv_obj=csv.reader(target_file)
# print(csv_obj)
mem=[]
for reco in csv_obj:
    a=[reco[DATA],reco[NAME],reco[RECO_TYPE],reco[RECO_TIME],reco[RECO_STATUE]]
    mem.append(a)
print(mem[1:])
name_type={}
for minzi in mem[1:]:
    name = minzi[1]
    name_type[name] = 0
for msg in mem[1:]:
    times=msg[0]
    week=datetime.strptime(times,"%Y/%m/%d").weekday()
    if week in (0,1,2,3,4):
        if msg[2]=="上班打卡" and msg[4]=="正常":
            if 0<=int((msg[3])[0:2])<9 or msg[3]=="09:00":
                name_type[msg[1]]+=1
        elif msg[2]=="下班打卡" and msg[4]=="正常":
            if 24>=int((msg[3])[0:2])>=21:
                name_type[msg[1]]+=1
    elif week ==5:
        if msg[2]=="上班打卡" and msg[4]=="正常":
            if 0<=int((msg[3])[0:2])<9 or msg[3]=="09:00":
                name_type[msg[1]]+=1
        elif msg[2]=="下班打卡" and msg[4]=="正常":
            if 24>=int((msg[3])[0:2])>=18:
                name_type[msg[1]]+=1
    elif week ==6:

        pass
    else:
        pass
print(name_type)







