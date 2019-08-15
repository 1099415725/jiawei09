# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/15   12:34
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
el1 = driver.find_element_by_id("android:id/button1")
el1.click()
time.sleep(4)
el2 = driver.find_element_by_id("com.miui.notes:id/menu_add")
el2.click()
time.sleep(4)
el3 = driver.find_element_by_id("com.miui.notes:id/rich_editor")
el3.send_keys("面对疾风吧！")


time.sleep(4)
el4 = driver.find_element_by_id("com.miui.notes:id/undo")
el4.click()
time.sleep(4)
el5 = driver.find_element_by_id("com.miui.notes:id/rich_editor")
el5.send_keys("一点寒芒先到，然后枪出如龙！")
time.sleep(4)
el6 = driver.find_element_by_id("com.miui.notes:id/more")
el6.click()
time.sleep(4)
el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.view.View")
el7.click()
time.sleep(4)
el8 = driver.find_element_by_id("com.miui.notes:id/more")
el8.click()
time.sleep(4)
el9 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[5]/android.view.View")
el9.click()
time.sleep(4)
el10 = driver.find_element_by_id("com.miui.notes:id/gallery")
el10.click()
time.sleep(4)
el11 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[2]")
el11.click()
time.sleep(4)
el12 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView")
el12.click()
time.sleep(4)
el13 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/miui.view.ViewPager/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.TextView")
el13.click()
time.sleep(4)
el14 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.GridView/android.widget.RelativeLayout[1]/android.widget.CheckBox")
el14.click()
time.sleep(4)
el15 = driver.find_element_by_id("android:id/button2")
el15.click()
time.sleep(4)
el16 = driver.find_element_by_id("com.miui.notes:id/home")
el16.click()