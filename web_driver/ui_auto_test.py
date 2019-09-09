# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/26   11:37
# 开发工具： PyCharm



import time
from selenium import webdriver


driver=webdriver.Firefox()

target_url="https://www.vip.com/"
driver.get(target_url)

search_sth=driver.find_element_by_xpath('/html/body/header/div/div/div[2]/div[1]/input')
search_sth.send_keys('华为')
search_click=driver.find_element_by_xpath('/html/body/header/div/div/div[2]/div[1]/a/span')
search_click.click()
time.sleep(2)

open_condition=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/button[1]/span[2]')
open_condition.



# driver.quit()