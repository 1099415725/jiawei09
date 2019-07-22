# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/19   19:45
# 文件名称： what_weekday.py
# 开发工具： PyCharm
from datetime import  datetime
today=datetime.now().weekday()
print(today)

week=datetime.strptime("2019-07-22","%Y-%m-%d").weekday()
print(week)
