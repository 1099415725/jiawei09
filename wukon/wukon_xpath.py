# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/17   11:39
# 开发工具： PyCharm

class Calculator:

    def __init__(self,driver):
        self.driver=driver

    @property
    def button_allowd_visit(self):
        element=self.driver.find_element_by_id("android:id/button1")
        return element

    @property
    def button_immediate_exp(self):
        elememt=self.driver.find_element_by_accessibility_id("立即体验")
        return elememt

    @property
    def button_username(self):
        element=self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[4]/android.view.View[1]/android.widget.EditText')
        return element

    @property
    def button_password(self):
        elememt = self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]/android.widget.EditText')
        return elememt

    @property
    def button_join(self):
        elememt = self.driver.find_element_by_accessibility_id("登录")
        return elememt

    @property
    def button_success_join(self):
        element=self.driver.find_element_by_xpath('//android.view.View[@content-desc="悟空CRM"]')
        return element

# 待办模块
    @property
    def button_agent_module(self):
        elememt = self.driver.find_element_by_xpath('//android.view.View[@content-desc="8 待办"]/android.view.View[1]')

        return elememt
    # 待办事项页面
    @property
    def button_agent_module_page(self):
        element=self.driver.find_element_by_xpath('//android.view.View[@content-desc="待办事项"]')
        return element

    # 即将到期的合同
    @property
    def button_contract_expire(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc=" 即将到期的合同 "]/android.view.View[2]')
        return element
    # 即将到期的合同页面确认
    @property
    def button_contract_expire_page(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc="即将到期的合同"]')
        return element


    # 即将到期的合同页面，返回
    @property
    def button_contract_expire_page_return(self):
        element = self.driver.find_element_by_xpath('//android.widget.Button[@content-desc=" "]')
        return element




    # 即将到期的合同.即将到期
    @property
    def button_about_to_expire(self):
        element = self.driver.find_element_by_xpath('	//android.view.View[@content-desc="即将到期"]')
        return element
    # 即将到期的合同.即将到期.即将到期
    @property
    def button_about_to_expire2(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc="即将到期"]')
        return element
    # 即将到期的合同.已到期
    @property
    def button_has_expire(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc="已到期"]')
        return element
    # 即将到期的合同.我的
    @property
    def button_mine(self):
        element = self.driver.finde_lement_by_xpath('//android.view.View[@content-desc="我的"]')
        return element
    # 即将到期的合同.我的.我的
    @property
    def button_mine_mine(self):
        element = self.driver.find_element_by_xpath('(//android.view.View[@content-desc="我的"])[2]')
        return element
    # 块属性（程咬金）
    @property
    def button_chengyaojing(self):
        element=self.driver.find_element_by_xpath('//android.view.View[@content-desc="程咬金 855555.00元 华为 待审核"]')
        return element
    # 即将到期的合同.我的.我下属的
    @property
    def button_mine_subordinate(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc="我下属的"]')
        return element

# crm模块
    @property
    def button_crm_modular(self):
        element = self.driver.find_element_by_xpath('(//android.view.View[@content-desc="CRM"])[1]/android.view.View[1]')
        return element

    # 回款模块
    @property
    def button_money_back(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc="回款"]')
        return element

    # 回款，添加
    @property
    def button_entry_tianjia(self):
        element = self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.Button[2]')
        return element

    # 回款界面，返回
    @property
    def button_huikuan_fanhui(self):
        element=self.driver.find_element_by_xpath('//android.widget.Button[@content-desc=" "]')

        return element

    # 成功进入回款界面，定位新建回款
    @property
    def button_success_in_huikuan(self):
        element=self.driver.find_element_by_xpath('//android.view.View[@content-desc="新建回款"]')
        return element
    #新建回款，返回
    @property
    def button_new_huikuan_return(self):
        element=self.driver.find_element_by_xpath('//android.widget.Button[@content-desc=" "]')
        return element
    # 新建回款，保存
    @property
    def button_new_huikuan_baocun(self):
        element = self.driver.find_element_by_xpath('')
        return element

    # 回款编号输入
    @property
    def button_huikuanbianhaoshuru(self):
        element=self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.EditText')
        return element
    # 客户名称界面
    @property
    def button_customer_name(self):
        element=self.driver.find_element_by_xpath('//android.view.View[@content-desc="选择客户名称"]')
        return element
    # 客户名称界面.华为
    @property
    def button_customer_interface_huawei(self):
        element=self.driver.find_element_by_xpath('//android.view.View[@content-desc="华为"]')
        return element
    # 选择客户名称界面，返回
    @property
    def button_customen_interface_return(self):
        element=self.driver.find_element_by_xpath('(//android.widget.Button[@content-desc=" "])[2]')
        return element
    # 选择合同编号界面
    @property
    def button_choice_contract(self):
        element=self.driver.find_element_by_xpath('	//android.view.View[@content-desc="选择合同编号"]')
        return element
    # 选择合同编号界面，ddd
    @property
    def button_choice_contract_ddd(self):
        element=self.driver.find_element_by_xpath('//android.view.View[@content-desc="ddd"]')
        return element
    # 选择合同界面，返回按钮
    @property
    def button_choice_contract_return(self):
        element=self.driver.find_element_by_xpath('(//android.widget.Button[@content-desc=" "])[2]')
        return element
    # 新建回款，回款日期
    @property
    def button_choice_contract_huikuan_date(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc="2019-08-19"]')
        return element


    # 新建回款，回款方式
    @property
    def button_choice_contract_huikuan_fangshi(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc="回款方式 "]/android.view.View/android.view.View[2]')
        return element

    # 新建回款，回款方式,现金
    @property
    def button_choice_contract_huikuan_fangshi_cash(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc="现金"]')
        return element

    ## 新建回款，回款方式,微信支付
    @property
    def button_choice_contract_huikuan_wcheat(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc="微信支付"]')
        return element
    # 新建回款，回款金额
    @property
    def button_choice_contract_huikuan_jinge(self):
        element = self.driver.find_element_by_xpath('//android.widget.EditText[@content-desc="元(必填)"]')
        return element



    # 新建回款，审核信息
    @property
    def button_choice_contract_shenhe_message(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc="+"]')
        return element

    # 选择审核人，管理员
    @property
    def button_choice_contract_shenhe_guanliyuan(self):
        element = self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[12]/android.view.View[2]/android.widget.ListView/android.view.View')
        return element




    # 回款查询
    @property
    def button_entry_select(self):
        element=self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.Button[1]')
        return element
    # 定位回款
    @property
    def button_dingwei_huikuan(self):
        element=self.driver.find_element_by_xpath('//android.view.View[@content-desc="回款"]')
        return element
    # 查询回款界面，取消
    @property
    def button_entry_quxiao(self):
        element=self.driver.find_element_by_xpath('//android.view.View[@content-desc="取消"]')
        return element




    # 产品模块
    # @property
    # def button_product(self):
    #     element = self.driver.findelement_by_xpath('//android.view.View[@content-desc="产品"]')
    #     return element
    # 进入产品页面，定位产品标题
    @property
    def button_jingru_chanping(self):
        element = self.driver.find_element_by_accessibility_id("产品")
        return element
    # 产品，添加
    @property
    def button_chanping_tianjia(self):
        element = self.driver.findelement_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.Button[2]')
                                                # //android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.Button[2]
        return element

    #新建产品界面
    @property
    def button_xinjian_chanping_page(self):
        element=self.driver.find_element_by_xpath('//android.view.View[@content-desc="新建产品"]')
        return element
    # 新建产品界面，返回
    @property
    def button_xinjian_chanping_page_return(self):
        element = self.driver.find_element_by_xpath('//android.widget.Button[@content-desc=" "]')
        return element

    # 新建产品界面，保存
    @property
    def button_xinjian_chanping_page_baocun(self):
        element = self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="保存"]')
        return element



    # 查询产品
    @property
    def button_chanping_chaxun(self):
        element = self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.Button[1]')
                                                # //android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.Button[1]
        return element
    # 查询产品。产品
    @property
    def button_chanping_chaxun_dingwei(self):
        element=self.driver.find_element_by_xpath('//android.view.View[@content-desc="产品"]')
        return element

    # 查询产品，取消
    @property
    def button_chanping_chaxun_quxiao(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc="取消"]')
        return element

    # 产品界面，返回按钮
    @property
    def button_chanping_fanhui(self):
        element = self.driver.findelement_by_xpath('//android.widget.Button[@content-desc=" "]')
        return element







    # 销售简报.本月
    @property
    def button_this_month(self):
        element = self.driver.findelement_by_xpath('')
        return element

# 办公模块
    @property
    def button_work_in_office(self):
        element = self.driver.find_element_by_xpath('(//android.view.View[@content-desc="办公"])[1]/android.view.View[1]')
        return element
    # 办公模块，办公
    @property
    def button_work_in_office_init(self):
        element = self.driver.find_element_by_xpath('	(//android.view.View[@content-desc="办公"])[1]')
        return element
    # 办公页面，日志
    @property
    def button_worn_bangon_rizhi(self):
        element=self.driver.find_element_by_xpath('//android.widget.Image[@content-desc="wkIsM2M+AkFmMxwgb21rgAAAABJRU5ErkJggg=="]')
        return element
    # 进入日志页面，日志定位
    @property
    def button_warn_bangon_rizhi_init(self):
        element=self.driver.find_element_by_xpath('//android.view.View[@content-desc="日志"]')
        return element
    # 日志页面，添加
    @property
    def button_warn_bangon_rizhi_tianjia(self):
        element=self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.Button')
        return element

    # 写日志
    @property
    def button_warn_bangon_rizhi_write(self):
        element=self.driver.find_element_by_xpath('//android.view.View[@content-desc="写日志"]')
        return element
    # 写日志，保存
    @property
    def button_warn_bangon_rizhi_write_baocun(self):
        element = self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="保存"]')
        return element

    # 写日志.今日工作内容
    @property
    def button_warn_bangon_rizhi_write_today(self):
        element = self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]')
        return element

    # 写日志.明日工作内容
    @property
    def button_warn_bangon_rizhi_write_tomorrow(self):
        element = self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]')
        return element

    # 写日志.问题
    @property
    def button_warn_bangon_rizhi_write_question(self):
        element = self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[3]')
        return element

    # 写日志.发送给谁
    @property
    def button_warn_bangon_rizhi_write_who(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc="+"]')
        return element
    # 写日志，选择用户，管理员
    @property
    def button_warn_rizhi_who_guanliyuan(self):
        element = self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ListView/android.view.View')
        return element

    # 确认新建日志成功，在明日工作内容中输入
    @property
    def button_warn_bangon_rizhi_write_success(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc="达尔文"]')
        return element



    # 办公页面，公告
    @property
    def button_work_bangon_gongao(self):
        element=self.driver.find_element_by_xpath('//android.widget.Image[@content-desc="fWsxWAAAAABJRU5ErkJggg=="]')
        return element

    #公告页面，公告
    @property
    def button_work_bangon_gongao_init(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc="公告"]')
        return element

    #公告页面，添加
    @property
    def button_work_bangon_gongao_add(self):
        element = self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.Button')
        return element




    # 公告页面，公示中
    @property
    def button_work_bangon_gongao_showing(self):
        element = self.driver.find_element_by_xpath('(//android.view.View[@content-desc="公示中"])[2]')
        return element

    # 公告页面，已结束
    @property
    def button_work_bangon_gongao_over(self):
        element = self.driver.findelement_by_xpath('(//android.view.View[@content-desc="已结束"])[2]')
        return element





# 我的模块
    @property
    def button_mine_modul(self):
        element = self.driver.find_element_by_xpayh('(//android.view.View[@content-desc="我的"])[1]/android.view.View[1]')
        return element


    # @property
    # def button_(self):
    #     element=self.drive.findelement_by_accessibility_id('')
    #     return element
    #
    # @property
    # def button_(self):
    #     element=self.drive.findelement_by_xpath('')
    #     return element

