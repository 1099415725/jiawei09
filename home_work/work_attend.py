# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/20   11:37
# 文件名称： work_attend.py
# 开发工具： PyCharm

import csv
from home_work.work_days import Work_days

# with open('C:/Users/Administrator/Desktop/work_time.csv', 'r',encoding="utf-8") as work_time:
#     data=csv.reader(work_time)
#     print(type(data))
#     time_list=[]
#     # print(data[0])
#     for i in data:
#         time_list.append(i)
#     print(time_list)
year_months = input("输入考勤年月,例如：（xxxx-xx)：\n")
coco = Work_days.get_work_days(year_months)

DATE = 0
NAME = 1
RECORD_TYPE = 5
RECORD_TIME = 6
target_file = open("work_time.csv", encoding="UTF-8")
csv_obj = csv.reader(target_file)

to_work_least = []
off_work_least = []
for record in csv_obj:
    work_list = [record[DATE], record[NAME], record[RECORD_TYPE], record[RECORD_TIME]]
    if work_list[2] == "上班打卡":
        to_work_least.append(work_list)
    elif work_list[2] == "下班打卡":
        off_work_least.append(work_list)
print(to_work_least)
print(off_work_least)
# 判断是否正常出勤，迟到时间，早退时间
final_work_least = []
for work_time in to_work_least:
    for free_time in off_work_least:
        if work_time[0] == free_time[0] and work_time[1] == free_time[1]:
            work_time.append(free_time[2])
            work_time.append(free_time[3])
            final_work_least.append(work_time)
            # print(final_work_least)
            # 判断是否正常出勤，迟到时间，早退时间
            if work_time[3] == "--" and work_time[5] == "--":
                work_time.append("非正常出勤")
                work_time.append("缺卡")
                work_time.append("缺卡")
            elif work_time[3] == "--" and work_time[5] != "--":
                work_time.append("非正常出勤")
                work_time.append("缺卡")
                c = int((work_time[5])[0:2])
                a = int(work_time[5][3:5])
                if c < 21:
                    minut = (21 - c) * 60 - a
                    work_time.append(minut)
                else:
                    work_time.append(0)
            elif work_time[3] != "--" and work_time[5] == "--":
                work_time.append("非正常出勤")
                c = int((work_time[3])[0:2])
                a = int(work_time[3][3:5])
                if c >= 9:
                    minut = (c - 9) * 60 + a
                    work_time.append(minut)
                    work_time.append("缺卡")
                else:
                    work_time.append(0)
                    work_time.append("缺卡")
            elif work_time[3] != "--" and work_time[5] != "--":
                if int((work_time[3])[0:2]) <= 8 and int(work_time[5][0:2]) >= 21:
                    work_time.append("正常出勤")
                    work_time.append(0)
                    work_time.append(0)
                elif int((work_time[3])[0:2]) <= 8 and int(work_time[5][0:2]) < 21:
                    work_time.append("非正常出勤")
                    work_time.append(0)
                    minut = (21 - int(work_time[5][0:2])) * 60 - int(work_time[5][3:5])
                    work_time.append(minut)
                elif (work_time[3])[0:2] == "09" and (work_time[3])[3:5] == "00" and int(work_time[5][0:2]) >= 21:
                    work_time.append("正常出勤")
                    work_time.append(0)
                    work_time.append(0)
                elif (work_time[3])[0:2] == "09" and (work_time[3])[3:5] == "00" and int(work_time[5][0:2]) < 21:
                    work_time.append("非正常出勤")
                    work_time.append(0)
                    minut = int(21 - int(work_time[5][0:2])) * 60 - int(work_time[5][3:5])
                    work_time.append(minut)
                elif int((work_time[3])[0:2]) >= 9 and int((work_time[3])[3:5]) > 0 and int(work_time[5][0:2]) >= 21:
                    work_time.append("非正常出勤")
                    minut = int(int((work_time[3])[0:2]) - 9) * 60 + int((work_time[3])[3:5])
                    work_time.append(minut)
                    work_time.append(0)
                elif int((work_time[3])[0:2]) >= 9 and int((work_time[3])[3:5]) > 0 and int(work_time[5][0:2]) < 21:
                    work_time.append("非正常出勤")
                    minut = int(int((work_time[3])[0:2]) - 9) * 60 + int((work_time[3])[3:5])
                    work_time.append(minut)
                    minut1 = int(21 - int(work_time[5][0:2])) * 60 - int(work_time[5][3:5])
                    work_time.append(minut1)

# 每日 缺勤统计
# print(final_work_least)
free_day = final_work_least
for times in free_day:
    a = times[7]
    b = times[8]
    if times[7] == "缺卡" and times[8] == "缺卡":
        times.append(1)
    elif times[7] != "缺卡" and times[8] == "缺卡":
        if times[7] > 30:
            times.append(1)
        else:
            times.append(0.5)
    elif times[7] == "缺卡" and times[8] != "缺卡":
        if times[8] > 30:
            times.append(1)
        else:
            times.append(0.5)
    elif a != "缺卡" and b != "缺卡":
        if int(a) > 30 and int(b) > 30:
            times.append(1)
        elif int(times[7]) > 30 or int(times[8]) > 30:
            times.append(0.5)
        elif int(times[7]) <= 30 and int(times[8]) <= 30:
            times.append(0)

    print(times)
# print(free_day)

# 取出统计之后的员工姓名和总缺勤天数
mems_dict = {}
for mems in free_day:
    mems_key = mems[1]
    mems_value = 0
    mems_dict[mems_key] = 0
# print(mems_dict)
for mem in mems_dict.items():
    # print (mem[0])
    aa = mem[0]
    cc = mem[1]
    for mem1 in free_day:

        if mem[0] == mem1[1]:
            cc += mem1[-1]
            mems_dict[aa] = cc

# 格式化输出和计算工资系数
attend_list = []
for name, date in mems_dict.items():
    # print(name,date)
    act_day = coco - date
    money = act_day / coco
    final_result = year_months, name, date, coco, act_day, money
    attend_list.append(final_result)
print("考勤年月", "员工姓名", "  缺勤天数", "应出勤天数", "实际出勤天数", "工资系数")
for i in attend_list:
    print("%s\t  %s\t   %s\t   %s\t %s\t   %.3f" % (i[0], i[1], i[2], i[3], i[4], i[5]))
# print(attend_list)
