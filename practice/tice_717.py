# encoding ：UTF-8
# 开发团队：  DanceFlower
# 开发人员： 张伟
# 开发时间： 2019/7/17   22:46
# 文件名称： tice_717.py
# 开发工具： PyCharm
import time

dt = time.localtime()
ft = "%Y-%m-%d"
nt = time.strftime(ft, dt)
currency = "人民币"

shop_list = [["交易日期", "消费类型", "金额", "币种", "余额"], ["2019/07/16", "转入", 2000, "人民币", 2000]]
print("%s   \t %s  \t  %s   \t %s   \t %s " % (
            shop_list[0][0], shop_list[0][1], shop_list[0][2], shop_list[0][3], shop_list[0][4]))


class Bank:
    '''
    date；消费的日期
    type:消费的类型
    amount:消费金额
    currency:币种
    blance:余额
    '''

    # 转入金额
    @classmethod
    def into_money(cls, money):
        date = nt
        type = "转入"
        amount = money
        blance = (shop_list[1])[-1] + amount
        shop_data = [date, type, amount, currency, blance]
        shop_list.insert(1, shop_data)
        print("%s \t %s    \t  +%s   \t %s   \t %s " % (
            shop_list[1][0], shop_list[1][1], shop_list[1][2], shop_list[1][3], shop_list[1][4]))

    @classmethod
    def cons_money(cls, money):
        date = nt
        type = "消费"
        amount = money
        blance = (shop_list[1])[-1] - amount
        shop_data = [date, type, amount, currency, blance]
        shop_list.insert(1, shop_data)
        print("%s \t %s    \t  -%s   \t %s   \t %s " % (
            shop_list[1][0], shop_list[1][1], shop_list[1][2], shop_list[1][3], shop_list[1][4]))

    @classmethod
    def net_money(cls, money):
        date = nt
        type = "网转"
        amount = money
        blance = (shop_list[1])[-1] - amount
        shop_data = [date, type, amount, currency, blance]
        shop_list.insert(1, shop_data)
        print("%s \t %s    \t  -%s   \t %s   \t %s " % (
            shop_list[1][0], shop_list[1][1], shop_list[1][2], shop_list[1][3], shop_list[1][4]))


shopping = Bank.into_money(5000)
consumption = Bank.cons_money(1000)
networking = Bank.net_money(2000)
networking = Bank.net_money(2000)
networking = Bank.net_money(1000)
