# encoding ：UTF-8
# 开发团队：  DanceFlower
# 开发人员： 张伟
# 开发时间： 2019/7/21   19:57
# 文件名称： work_days.py
# 开发工具： PyCharm
from datetime import datetime
today = datetime.now().weekday()
class Work_days:

    @classmethod
    def get_work_days(cls,year_months):
        mouths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year_month=year_months
        # today = datetime.now().weekday()
        # print(today)

        week = datetime.strptime("2019-07-21", "%Y-%m-%d").weekday()
        # print(type(week))
        # 判断某年的某个月份需要工作多少天
        # year_month = input("输入考勤年月（年份-月份）：\n")
        if int(year_month[5:]) in (1, 3, 5, 7, 8, 10, 12):
            new_month = year_month + "-01"
            week = datetime.strptime(new_month, "%Y-%m-%d").weekday()
            if week >= 4:
                act_work_day = 26
                return act_work_day

            elif week < 4:
                act_work_day = 27
                return act_work_day

        elif int(year_month[5:]) in (4, 6, 9, 11):
            new_month = year_month + "-01"
            week = datetime.strptime(new_month, "%Y-%m-%d").weekday()
            if week >= 5:
                act_work_day = 25
                return act_work_day

            elif week < 5:
                act_work_day = 26
                return act_work_day

        elif int(year_month[0:4]) % 4 == 0 and int(year_month[0:4]) % 100 != 0:
            if year_month[5:] == "02":
                new_month = year_month + "-01"
                week = datetime.strptime(new_month, "%Y-%m-%d").weekday()
                if week == 6:
                    act_work_day = 24
                    return act_work_day

                elif week != 6:
                    act_work_day = 25
                    return act_work_day

        elif int(year_month[0:4]) % 4 != 0:
            if year_month[5:] == "02":
                act_work_day = 24
                return act_work_day


if __name__=="__main__":

    mm=Work_days.get_work_days()