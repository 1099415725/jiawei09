# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/19   15:25
# 开发工具： PyCharm

import time

class ActLogin():
    def __init__(self,driver):
        self.driver=driver

    @property
    def po_username(self):
        # while i<10:
        #     i+=0.5
            try:
                element = self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[4]/android.view.View[1]/android.widget.EditText')

            except:
                print("NO element found！sleep 3s")
                time.sleep(3)
                element = self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[4]/android.view.View[1]/android.widget.EditText')

            return element