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
    'Cookie': 'aws-priv=eyJ2IjoxLCJldSI6MCwic3QiOjB9; aws_lang=cn; skin=noskin; lc-main=en_US; x-wl-uid=1p0UZ5/lCbkNROR+xWiSnPGuFyGlRwp86OdmSIFR0U1TTOebby+pvHxhdOz/LhXS3naZ/LPH/QmEVu0EHSOiU09lTwn8W63qe+iaavH/4YcymZtQDbNoai6gW6ZlWf+38Yp13xahQggI=; original-session-id=137-1599583-2548311; session-id=146-8901077-5508928; ubid-main=133-1843048-7886153; aws-target-static-id=1580931802401-448324; aws-target-data=%7B%22support%22%3A%221%22%7D; s_fid=50CB35CE83132A9B-3056ED195E08A140; aws-target-visitor-id=1580931802403-807069.17_0; aws-ubid-main=442-7472065-3144747; aws-reg-aid=858789323577; aws-reg-guid=844020028bec9c00601251df23fe53ae9baca11e2a0423d2abb90591824bbae4; aws-business-metrics-last-visit=1581736302175; regStatus=registered; aws-mkto-trk=id%3A112-TZM-766%26token%3A_mch-aws.amazon.com-1581832886902-29417; c_m=undefinedwww.google.comSearch%20Engine; pN=6; s_pers=%20s_nr%3D1581834648873-Repeat%7C1589610648873%3B; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3Dawsamazonallprod1%252Cawsamazonregprod1%252Cawsamazonregprod2%252Cawsamazonallprod2%253D%252526pid%25253Dawsjavasdk%2525252Flatest%2525252Fjavadoc%2525252Fcom%2525252Famazonaws%2525252Fservices%2525252Fsns%2525252Famazonsns%252526pidt%25253D1%252526oid%25253Dhttps%2525253A%2525252F%2525252Fdocs.aws.amazon.com%2525252Fsns%2525252Flatest%2525252Fdg%2525252F%252526ot%25253DA%3B; s_cc=true; s_sq=%5B%5BB%5D%5D; noflush_locale=zh_CN; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A858789323577%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22Louyilin%22%2C%22keybase%22%3A%22kZmCVS4GGeqn2eHn0NZuWMKwuR%2FS%2FopxiTg3%2F7P0BuM%5Cu003d%22%2C%22issuer%22%3A%22http%3A%2F%2Fsignin.aws.amazon.com%2Fsignin%22%2C%22signinType%22%3A%22PUBLIC%22%7D; x-main="8IT9vyjnwPVPa1X07KFFS9Q?8zVkLv5k@5Deulq2mry1dyovejKarKayYEorWC7I"; at-main=Atza|IwEBIGXTBsWM6wBWAider7SckYqQpWFSn3GZRNrTYTV8_RkuelkiIR_BA2YTmB1wpgJt0kg5zLZDq9jr8TzUfcJ09izfXgFk6Nu0IwzBoeY6x2mxCTB28FQGmffdilCLr6ZBkC0omkti0FOWf1XBQyNTPeMttl0O5C0VOFvn6A8tH3yRrEUUKX_SXQYRy143OTdlMS2Nmg1tZKGpzaCl1hZDQ7Dn_YnKm61NK0lgyqzUxX96N4FbfKuodJZpVUaWR0se3qssdx_mPb898fXKX_LIkwIxYvDrwKb_sPbCe8zfTOqfB-2JdZBbGVDoFJdDkbNye4Gm5WIqTG0aOh8qAqyRtgFG1L2QhlBJM5oTt8XnIKagb2QpzQiqWX3mnThJRbBDpNG5ZwzDmXT9OUrzsUrXtD8g; sess-at-main="qRM3q3zl88uaKMq59LiVn5VMGHeD7HcOsnk5R6W3DzU="; sst-main=Sst1|PQEuqva_wfr1fbOmkrZtziTjCyTBySJl0T7Hcy6wstXH_8AndfGVBkvsIgMF8UyVRg8llmerjD9s8S5et5s8jZpkhSOb8PO8tpk3aQJBdYEheIFn6ORSs9iSfJdVCtsNUlXadrWubhlzKRO2JpFjN2EF_Ly5zHKkFeC4mzCfqYrUzZ5CD0CBd1TT6ip7u8-MJUSlOE-nDMvDuiITcTUkqJAXClbvyc0KQn_iusR1LxM3IwYcd-yWQJZmCk-LUghIHTNbZjupr52PVWIIgRPhmP-dkVTxbiRwFtoThDzK8aA6xMYkwtg_a8lv1lJCTN9A3Ma7Vwe73qbLdt--hgdMm58k4w; i18n-prefs=USD; s_vnum=2015869551948%26vn%3D2; s_ppv=100; cdn-session=AK-7fb2634e82941410d4ecbd3588ddd6e7; s_dslv=1586116992925; s_vn=1612467802673%26vn%3D9; s_nr=1586116992932-Repeat; session-id-time=2082787201l; session-token=aaCHAHJTTLFpgOIuNGI3aqsmaebxjomha93gL4f1GYEqmmHqnvmY6MPMGK80xf61m9VOS29MmZkF8VD05LwHP/X4IO2k4A4PL9kgX6TV1bWwWxnyBuyzeLTQv7a8i5V+yQvnbgCXYaYQIrXJUieoI+98uhvbYV7nn+XJgFMYWJzWu1A72NeCELf5qWuoukciPzkcKqUHJIfc6GfJWKfxfi8Rx9Xw9+rLwHxKXYmMykJFiqy1XxCsq5mkGFxT47gzoIkrEUNDUQXUV/6mdk1O9w==; csm-hit=tb:EQGZTYVQPV9TDK33ZBSZ+s-YKW60M8B0FZ9W837NGSP|1586138722724&t:1586138722724&adb:adblk_yes'

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
