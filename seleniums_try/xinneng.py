# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/9/4   19:50
# 开发工具： PyCharm
import unittest
import os
import re
import time
def coco():
    num=os.popen('adb shell dumpsys com.kakaroet.crm9').readlines()
    for i in num:
        if re.findall("TOTAL",i):
            momo=i.split(' ')
            while ' ' in momo:
                momo.remove('')
            meminfo=momo[1]
            return meminfo