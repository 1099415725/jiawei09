# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/14   17:36
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


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(7)
el1 = driver.find_element_by_id("android:id/button1")
el1.click()
time.sleep(7)
el2 = driver.find_element_by_id("com.miui.notes:id/menu_add")
el2.click()
time.sleep(7)
el3 = driver.find_element_by_id("com.miui.notes:id/rich_editor")
el3.send_keys("呵呵呵")
time.sleep(7)
el4 = driver.find_element_by_id("com.miui.notes:id/gallery")
el4.click()
time.sleep(7)
el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[2]")
el5.click()
time.sleep(7)
el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/miui.view.ViewPager/android.widget.FrameLayout/android.widget.GridView/android.widget.RelativeLayout[3]")
el6.click()
time.sleep(7)
el7 = driver.find_element_by_id("android:id/button2")
el7.click()
time.sleep(7)
el8 = driver.find_element_by_id("com.miui.notes:id/home")
el8.click()