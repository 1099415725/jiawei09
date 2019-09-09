# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/16   11:03
# 开发工具： PyCharm

import unittest
from appium import webdriver
import time
from applium_0814.calculators import calc
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['deviceName'] = '1204d2297d74'
        desired_caps['appPackage'] = 'com.candl.athenagcl'
        desired_caps['appActivity'] = '.activity.Calculator'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def test_1234_minus_2345(self):
        self.Calc.button_close.click()
        self.Calc.button_1.click()
        self.Calc.button_2.click()
        self.Calc.button_3.click()
        self.Calc.button_4.click()
        self.Calc.button_plus.click()
        self.Calc.button_2.click()
        self.Calc.button_3.click()
        self.Calc.button_4.click()
        self.Calc.button_5.click()
        self.Calc.button_equal.click()
        time.sleep(1)
        act_result=self.Calc.button_result.text
        exp_result="3,579"
        self.assertEqual(act_result, exp_result)


