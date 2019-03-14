'''
模拟豆瓣登录
url = 'https://www.douban.com/'
user:19938467368
password:Huawei12#$

'''


from selenium import webdriver

driver = webdriver.PhantomJS()

driver.get('https://www.douban.com/')
driver.maximize_window()  # 浏览器窗口等于屏幕大小
driver.implicitly_wait(5)


driver.find_element_by_id('form_email').clear()
driver.find_element_by_id('form_email').send_keys('19938467368')
driver.find_element_by_id('form_password').clear()
driver.find_element_by_id('form_password').send_keys('Huawei12#$')
driver.find_element_by_class_name('bn-submit').click()

driver.implicitly_wait(1)

with open('/home/tlxy/tulingxueyuan/xuexi/DHTML/img/douban.html','w',encoding='utf-8') as f:
    f.write(driver.page_source)

# 获取当前地址
print(driver.current_url)