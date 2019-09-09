import unittest
from selenium import webdriver
import time

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        url="http://47.92.220.226/webdriver"
        cls.driver.get(url)
    def test_iframDemo(self):
        self.driver.find_element_by_xpath('/html/body/ul/li[4]/a').click()
        time.sleep(2)
        # 双重定位
        frameset_demo=self.driver.find_element_by_tag_name("frameset")
        # leftfram_demo=frameset_demo.find_element_by_id("leftfram")
        middlefram_demo=frameset_demo.find_element_by_id("middlefram")
        # 切换到中间的frame
        self.driver.switch_to.frame(middlefram_demo)
        # 获取当前窗口
        current_window=self.driver.current_window_handle
        #切换当前窗口
        self.driver.switch_to.window(current_window)
        # 定位ifram
        ifram_demo=self.driver.find_element_by_id("ifram")
#         切换到ifram窗口
        self.driver.switch_to.frame(ifram_demo)
#         输入标题
        self.driver.find_element_by_xpath('//*[@id="note_title"]').send_keys(u'忘情水是谁给的')
#         输入内容
        self.driver.find_element_by_xpath('/html/body/div/textarea').send_keys(u'你猜啊！')



if __name__ == '__main__':
    unittest.main()
