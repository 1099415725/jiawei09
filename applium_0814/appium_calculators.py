#encoding:utf-8

import unittest
from appium import webdriver
import time
from applium_0814.calculators import Calculator


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
        time.sleep(2)
        cls.calc=Calculator(cls.driver)

    def test_1_plus(self):
        self.calc.button_close.click()
        time.sleep(3)
        self.calc.button_1.click()
        self.calc.button_2.click()
        self.calc.button_0.click()
        self.calc.button_0.click()
        self.calc.button_plus.click()
        self.calc.button_2.click()
        self.calc.button_0.click()
        self.calc.button_0.click()
        self.calc.button_0.click()
        self.calc.button_equal.click()
        time.sleep(1)
        act_result=self.calc.button_result.text
        exp_result=u"3,200"
        self.assertEqual(act_result, exp_result)
        time.sleep(3)
        self.calc.button_clear.click()

    def test_2_minus(self):

        self.calc.button_2.click()
        self.calc.button_2.click()
        self.calc.button_3.click()
        self.calc.button_4.click()
        self.calc.button_minus.click()
        self.calc.button_1.click()
        self.calc.button_2.click()
        self.calc.button_0.click()
        self.calc.button_0.click()
        self.calc.button_equal.click()
        time.sleep(1)
        act_result=self.calc.button_result.text
        exp_result=u"1,034"
        self.assertEqual(act_result, exp_result)
        time.sleep(3)
        self.calc.button_clear.click()

    def test_3_mul(self):

        self.calc.button_1.click()
        self.calc.button_2.click()
        self.calc.button_3.click()
        self.calc.button_4.click()
        self.calc.button_mul.click()
        self.calc.button_2.click()
        self.calc.button_0.click()
        self.calc.button_0.click()
        self.calc.button_0.click()
        self.calc.button_equal.click()
        time.sleep(1)
        act_result=self.calc.button_result.text
        exp_result=u"2,468,000"
        self.assertEqual(act_result, exp_result)
        time.sleep(3)
        self.calc.button_clear.click()

    def test_4_div(self):
        self.calc.button_clear.click()
        self.calc.button_1.click()
        self.calc.button_2.click()
        self.calc.button_0.click()
        self.calc.button_0.click()
        self.calc.button_div.click()
        self.calc.button_6.click()
        self.calc.button_0.click()
        self.calc.button_equal.click()
        time.sleep(1)
        act_result=self.calc.button_result.text
        exp_result=u"20"
        self.assertEqual(act_result, exp_result)
        time.sleep(3)
        self.calc.button_clear.click()


if __name__ == '__main__':
    unittest.main()
