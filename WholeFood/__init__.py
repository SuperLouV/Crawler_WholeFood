import os

from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests

# 加载项目所用包
# 在浏览器-开发者工具-netwark-刷新页面-第一个链接中的request headers-cookies   复制cookie到下面
# 运行程序,会打开一个浏览器页面，自行输入用户名，密码，一直continue，知道预定时间的页面


driver = webdriver.Chrome()
driver.maximize_window()  # 最大化窗口
driver.implicitly_wait(3)
url = "https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Referer': 'https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1',
    # cookies复制到这里，如果该代码输出为空，更新这个cookie
    'Cookie': '复制到这里'

}
driver.get(url)  # 加载url

# cookies=driver.get_cookies()
# print(cookies)
Check_Statues = True
response = requests.get(url, headers=headers)
html_str = response.content.decode('utf-8')
html = etree.HTML(html_str)

while Check_Statues:
    try:
        driver.refresh()
        print("refreshed")
        print(time.ctime())  # time

        # 开始获取值
        if_availability = html.xpath(
            '//div[@class="a-row ufss-widget-grid-row"]//div[@class="ufss-date-select-toggle-text-availability"]//text()')
        print(if_availability)
        days_availability = html.xpath(
            '//*[@class="ufss-date-select-toggle-text-month-day"]//text()')
        print(days_availability)

        for i in if_availability:
            i = str(i).strip()
            if (i == 'Not available'):
                print("没有位置")
                os.system('say "没有位置"')

            else:
                print("有位置")
                os.system('say "有位置了,快抢"')
        time.sleep(40)  # 页面刷新时常 单位秒
    except:
        print("error")
