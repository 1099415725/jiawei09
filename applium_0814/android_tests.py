# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/15   15:41
# 开发工具： PyCharm

from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['deviceName'] = '1204d2297d74'
desired_caps['appPackage'] = 'com.miui.notes'
desired_caps['appActivity'] = '.ui.NotesListActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(4)
ele=driver.find_element_by_id("android:id/button1")
ele.click()

time.sleep(4)
ele=driver.find_element_by_id("com.miui.notes:id/menu_add")
ele.click()
time.sleep(4)

ele=driver.find_element_by_id("com.miui.notes:id/rich_editor")
ele.send_keys(u"但愿日子清净")
time.sleep(4)


ele=driver.find_element_by_id("com.miui.notes:id/home")
ele.click()
