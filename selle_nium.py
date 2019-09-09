# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/9/2   10:42
# 开发工具： PyCharm

from selenium import webdriver
import time
driver=webdriver.Firefox()
url=driver.get('http://www.baidu.com')

dingwei=driver.find_element_by_xpath('//*[@id="kw"]')
dingwei.send_keys(u'詹姆斯')
search_click=driver.find_element_by_xpath('//*[@id="su"]')
search_click.click()
time.sleep(10)

h3_titles=driver.find_elements_by_tag_name('h3')
for title in h3_titles:
    print (title.text)

driver.quit()


