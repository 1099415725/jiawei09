# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/15   17:35
# 开发工具： PyCharm

from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['deviceName'] = '1204d2297d74'
desired_caps['appPackage'] = 'com.candl.athenagcl'
desired_caps['appActivity'] = '.activity.Calculator'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(3)

first_page=driver.find_element_by_id("com.candl.athenagcl:id/btn_close")
first_page.click()
time.sleep(3)

first_page=driver.find_element_by_id("com.candl.athenagcl:id/digit4")
first_page.click()
time.sleep(3)

first_page=driver.find_element_by_id("com.candl.athenagcl:id/digit3")
first_page.click()
time.sleep(3)

first_page=driver.find_element_by_id("com.candl.athenagcl:id/digit2")
first_page.click()
time.sleep(3)

first_page=driver.find_element_by_id("com.candl.athenagcl:id/digit1")
first_page.click()
time.sleep(3)

first_page=driver.find_element_by_id("com.candl.athenagcl:id/plus")
first_page.click()
time.sleep(3)

first_page=driver.find_element_by_id("com.candl.athenagcl:id/digit1")
first_page.click()
time.sleep(3)

first_page=driver.find_element_by_id("com.candl.athenagcl:id/digit2")
first_page.click()
time.sleep(3)

first_page=driver.find_element_by_id("com.candl.athenagcl:id/digit3")
first_page.click()
time.sleep(3)

first_page=driver.find_element_by_id("com.candl.athenagcl:id/digit4")
first_page.click()
time.sleep(3)

first_page=driver.find_element_by_id("com.candl.athenagcl:id/equal")
first_page.click()
time.sleep(4)




