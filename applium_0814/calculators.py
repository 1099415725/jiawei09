# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/16   11:32
# 开发工具： PyCharm

class Calculator:

    def __init__(self,driver):
        self.driver=driver

    @property
    def button_1(self):
        element=self.driver.find_element_by_id("com.candl.athenagcl:id/digit1")
        return element

    @property
    def button_2(self):
        element = self.driver.find_element_by_id("com.candl.athenagcl:id/digit2")
        return element

    @property
    def button_3(self):
        element = self.driver.find_element_by_id("com.candl.athenagcl:id/digit3")
        return element

    @property
    def button_4(self):
        element = self.driver.find_element_by_id("com.candl.athenagcl:id/digit4")
        return element

    @property
    def button_5(self):
        element = self.driver.find_element_by_id("com.candl.athenagcl:id/digit5")
        return element

    @property
    def button_6(self):
        element = self.driver.find_element_by_id("com.candl.athenagcl:id/digit6")
        return element

    @property
    def button_7(self):
        element = self.driver.find_element_by_id("com.candl.athenagcl:id/digit7")
        return element

    @property
    def button_8(self):
        element = self.driver.find_element_by_id("com.candl.athenagcl:id/digit8")
        return element

    @property
    def button_9(self):
        element = self.driver.find_element_by_id("com.candl.athenagcl:id/digit9")
        return element

    @property
    def button_0(self):
        element = self.driver.find_element_by_id("com.candl.athenagcl:id/digit0")
        return element

    @property
    def button_plus(self):
        element = self.driver.find_element_by_id("com.candl.athenagcl:id/plus")
        return element

    @property
    def button_minus(self):
        element = self.driver.find_element_by_id("com.candl.athenagcl:id/minus")
        return element

    @property
    def button_mul(self):
        element = self.driver.find_element_by_id("com.candl.athenagcl:id/mul")
        return element

    @property
    def button_div(self):
        element = self.driver.find_element_by_id("com.candl.athenagcl:id/div")
        return element

    @property
    def button_equal(self):
        element = self.driver.find_element_by_id("com.candl.athenagcl:id/equal")
        return element

    @property
    def button_result(self):
        element = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ViewSwitcher/android.widget.TextView")
        return element

    @property
    def button_clear(self):
        element = self.driver.find_element_by_id("com.candl.athenagcl:id/clear")
        return  element

    # 关闭首页引导
    @property
    def button_close(self):
        element = self.driver.find_element_by_id("com.candl.athenagcl:id/btn_close")
        return element

