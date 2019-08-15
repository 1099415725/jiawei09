import unittest
from appium import webdriver
import time

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
        time.sleep(3)

    # def setUp(self):
    #     first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/clear")
    #     first_page.click()
    #     time.sleep(3)

    def test_case01(self):
        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/btn_close")
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/digit4")
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/digit3")
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/digit2")
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/digit1")
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/plus")
        first_page.click()
        time.sleep(1)

        first_page =self. driver.find_element_by_id("com.candl.athenagcl:id/digit1")
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/digit2")
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/digit3")
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/digit4")
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/equal")
        first_page.click()
        time.sleep(2)

        first_page1=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ViewSwitcher/android.widget.TextView")
        act_result=first_page1.text
        exp_result=u"5,555"
        self.assertEqual(act_result,exp_result)
        time.sleep(2)

    def test_case02(self):
        # first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/btn_close")
        # first_page.click()
        # time.sleep(3)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/clear")
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/digit4")
        first_page.click()
        time.sleep(1)
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/digit3")
        first_page.click()
        time.sleep(1)
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/minus")
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/digit3")
        first_page.click()
        time.sleep(1)
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/digit2")
        first_page.click()
        time.sleep(1)
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/equal")
        first_page.click()
        time.sleep(1)

        first_page1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ViewSwitcher/android.widget.TextView")
        act_result = first_page1.text
        exp_result = u"1,111"
        self.assertEqual(act_result, exp_result)
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/clear")
        first_page.click()
        time.sleep(1)

    def test_case03(self):
        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/clear")
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/digit4")
        first_page.click()
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/digit3")
        first_page.click()
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/mul")
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/digit2")
        first_page.click()

        time.sleep(1)

        first_page1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ViewSwitcher/android.widget.TextView")
        act_result = first_page1.text
        exp_result = u"8,866"
        self.assertEqual(act_result, exp_result)
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/clear")
        first_page.click()
        time.sleep(1)

    def test_case04(self):

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/digit4")
        first_page.click()
        first_page.click()
        first_page.click()
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/div")
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/digit4")
        first_page.click()
        first_page.click()
        first_page.click()
        first_page.click()
        time.sleep(1)

        first_page = self.driver.find_element_by_id("com.candl.athenagcl:id/equal")
        first_page.click()
        time.sleep(1)

        first_page1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ViewSwitcher/android.widget.TextView")
        act_result = first_page1.text
        exp_result = u"1"
        self.assertEqual(act_result, exp_result)
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()
