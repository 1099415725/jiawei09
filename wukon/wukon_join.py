# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/17   11:40
# 开发工具： PyCharm

import unittest
from appium import webdriver
import time
from wukon.wukon_xpath import Calculator
from wukon import config
from wukon.act_login import ActLogin


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = config.platformName
        desired_caps['platformVersion'] = config.platformVersion
        desired_caps['automationName'] = config.automationName
        desired_caps['deviceName'] = config.deviceName
        desired_caps['appPackage'] = config.appPackage
        desired_caps['appActivity'] = config.appActivity
        desired_caps['unicodeKeyboard'] = config.unicodeKeyboard
        desired_caps['resetKeyboard'] = config.resetKeyboard
        desired_caps['noReset']=config.noReset
        interface='http://%s:%s/wd/hub'%(config.COST_IP,config.COST_PORT)
        cls.driver = webdriver.Remote(interface, desired_caps)
        time.sleep(5)
        cls.calc=Calculator(cls.driver)
        time.sleep(3)
        # cls.calc.button_allowd_visit.click()
        # time.sleep(5)
        # cls.calc.button_immediate_exp.click()
        # time.sleep(4)
        cls.ActLogin=ActLogin
        cls.ActLogin.po_username

        cls.calc.button_username.send_keys("13419591290")
        time.sleep(3)
        cls.calc.button_password.send_keys("zhang08109212")
        time.sleep(3)
        cls.calc.button_join.click()
        time.sleep(3)
    # 确认登录成功
    def test_01_success_in_expire(self):
        # self.calc.button_success_join
        act_result=self.calc.button_success_join.get_attribute('contentDescription')
        exp_result=u'悟空CRM'
        self.assertEqual(act_result, exp_result)
        time.sleep(4)

    # 进入回款界面成功
    def test_02_entry_return(self):
        self.calc.button_money_back.click()
        act_result=self.calc.button_money_back.get_attribute('contentDescription')
        exp_result=u'回款'
        self.assertEqual(act_result, exp_result)
        time.sleep(3)


    # 进入新建回款界面成功
    def test_03_jinru_new_repament(self):
        self.calc.button_entry_tianjia.click()
        time.sleep(2)
        act_result=self.calc.button_success_in_huikuan.get_attribute('contentDescription')
        exp_result=u'新建回款'
        self.assertEqual(act_result, exp_result)
        time.sleep(2)
        self.calc.button_new_huikuan_return.click()
        time.sleep(2)

    # 新建回款信息
    # def test_04_xinjianhuikuan_message(self):
    #     self.calc.button_huikuanbianhaoshuru.send_key('2020520')
    #     self.calc.button_customer_name.click()
    #     time.sleep(1)
    #     self.calc.button_customer_interface_huawei.click()
    #     self.calc.button_new_huikuan_return.click()
    #     self.calc.button_choice_contract.click()
    #     time.sleep(1)
    #     self.calc.button_choice_contract_ddd.click()
    #     self.calc.button_choice_contract.click()
    #     self.calc.button_choice_contract_huikuan_fangshi.click()
    #     time.sleep(1)
    #     self.calc.button_choice_contract_huikuan_fangshi_cash.click()
    #     self.calc.button_choice_contract.click()
    #     time.sleep(1)
    #     self.calc.button_choice_contract_huikuan_jinge.senf_key('20000')
    #     self.calc.button_choice_contract_shenhe_message.click()
    #     time.sleep(1)
    #     self.calc.button_choice_contract_shenhe_guanliyuan.click()
    #     self.calc.button_choice_contract.click()
    #     self.calc.button_new_huikuan_baocun
    #     self.calc.button_choice_contract.click()




    # 进入回款查询界面
    def test_04_huikuan_chaxun(self):
        self.calc.button_entry_select.click()
        time.sleep(1)
        act_result=self.calc.button_dingwei_huikuan.get_attribute('contentDescription')
        exp_result=u'回款'
        self.assertEqual(act_result, exp_result)
        self.calc.button_entry_quxiao.click()
        time.sleep(2)
        self.calc.button_huikuan_fanhui.click()


    # 进入产品界面
    def test_05_jinru_chanping_jiemian(self):
        time.sleep(2)
        self.calc.button_jingru_chanping.click()
        time.sleep(2)
        act_result = self.calc.button_jingru_chanping.get_attribute('contentDescription')
        exp_result = u'产品'
        self.assertEqual(act_result, exp_result)


    # 进入到添加产品界面
    def test_06_jinru_tianjia_chanping(self):
        time.sleep(2)
        self.calc.button_entry_tianjia.click()
        time.sleep(2)
        act_result = self.calc.button_xinjian_chanping_page.get_attribute('contentDescription')
        exp_result = u'新建产品'
        self.assertEqual(act_result, exp_result)
        self.calc.button_huikuan_fanhui.click()





    # 进入到查询产品界面
    def test_07_jinru_chanping_chaxun(self):
        time.sleep(2)
        self.calc.button_chanping_chaxun.click()
        time.sleep(2)
        act_result = self.calc.button_chanping_chaxun_dingwei.get_attribute('contentDescription')
        exp_result = u'产品'
        self.assertEqual(act_result, exp_result)
        self.calc.button_chanping_chaxun_quxiao.click()
        time.sleep(1)
        self.calc.button_xinjian_chanping_page_return.click()


    # 进入到待办模块
    def test_08_jinru_daiban(self):
        time.sleep(5)
        self.calc.button_agent_module.click()
        time.sleep(3)
        act_result = self.calc.button_agent_module_page.get_attribute('contentDescription')
        exp_result = u'待办事项'
        self.assertEqual(act_result, exp_result)


    # 进入到即将到期的合同界面
    def test_09_jijian_daoqi_heton(self):
        time.sleep(2)
        self.calc.button_contract_expire.click()
        time.sleep(2)
        act_result = self.calc.button_contract_expire_page.get_attribute('contentDescription')
        exp_result = u'即将到期的合同'
        self.assertEqual(act_result, exp_result)


    # 能够查询到已到期的合同
    def test_10_yidaoqi_heton(self):
        self.calc.button_about_to_expire.click()
        time.sleep(1)
        self.calc.button_has_expire.click()
        time.sleep(2)
        act_result=self.calc.button_chengyaojing.get_attribute('contentDescription')
        exp_result=u'程咬金 855555.00元 华为 待审核'
        self.assertEqual(act_result, exp_result)
        time.sleep(2)
        self.calc.button_contract_expire_page_return.click()

    # 进入到办公模块
    def test_11_work_mokuai(self):
        time.sleep(1)
        self.calc.button_work_in_office.click()
        time.sleep(2)
        act_result = self.calc.button_work_in_office_init.get_attribute('contentDescription')
        exp_result = u'办公'
        self.assertEqual(act_result, exp_result)
    # 进入日志模块
    def test_12_work_rizhi(self):
        self.calc.button_worn_bangon_rizhi.click()
        time.sleep(1)
        act_result = self.calc.button_warn_bangon_rizhi_init.get_attribute('contentDescription')
        exp_result = u'日志'
        self.assertEqual(act_result, exp_result)

    # 进入日志，添加模块
    def test_13_work_rizhi_tianjia(self):
        self.calc.button_warn_bangon_rizhi_tianjia.click()
        time.sleep(1)
        act_result=self.calc.button_warn_bangon_rizhi_write.get_attribute('contentDescription')
        exp_result = u'写日志'
        self.assertEqual(act_result, exp_result)

    # 添加日志
    def test_14_work_rizhi_tianjia_success(self):
        self.calc.button_warn_bangon_rizhi_write_tomorrow.send_keys('达尔文')
        time.sleep(1)
        self.calc.button_warn_bangon_rizhi_write_baocun.click()
        time.sleep(1)
        act_result=self.calc.button_warn_bangon_rizhi_write_success.get_attribute('contentDescription')
        exp_result = u'达尔文'
        self.assertEqual(act_result, exp_result)











































    # 进入待办事项模块
    # def test_2_success_in_daiban(self):
    #     self.calc.button_agent_module.click()
    #     time.sleep(3)
    #     self.calc.button_agent_module_page
    #     act_result=self.calc.button_agent_module_page.get_attribute('contentDescription')
    #     exp_result = u"待办事项"
    #     self.assertEqual(act_result, exp_result)
    #     time.sleep(3)

    # def test_2_determine_successful_login(self):
    #     self.calc.button_agent_module.click()
    #     time.sleep(5)
    #     self.calc.button_contract_expire.click()
    #     time.sleep(5)
    #     self.calc.button_about_to_expire2.click()
    #     time.sleep(5)
    #     self.calc.button_has_expire.click()
    #     time.sleep(5)
    #     act_result = self.calc.button_chengyaojing.get_attribute('contentDescription')
    #     exp_result = u"程咬金 855555.00元 华为 待审核"
    #     self.assertEqual(act_result, exp_result)
    #     time.sleep(3)







if __name__ == '__main__':
    unittest.main()
