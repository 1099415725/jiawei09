# encoding:utf-8
import unittest
from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        try:
            cls.driver.implicitly_wait(10)
        except TimeoutException:
            print("页面加载超时！")
    def setUp(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
    def test_search_chs(self):
        driver=webdriver.Firefox()
        url="http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element_by_id("kw").send_keys(u"普金")
        self.driver.find_element_by_id("su").click()
        list_window=list()
        results=self.driver.find_elements_by_tag_name("h3")
        current_window=self.driver.current_window_handle
        for i in results:
            list_window.append(i.text)
        for i in list_window:
            self.driver.find_element_by_partial_link_text(i).click()
            print(self.driver.title)
            self.driver.switch_to.window(current_window)
        window_handle=self.driver.window_handles
        for i in window_handle:
            print("当前窗口的句柄是：",i)
            self.driver.switch_to.window(i)
            print("self.driver.title---->",self.driver.title)

if __name__ == '__main__':
    unittest.main()
