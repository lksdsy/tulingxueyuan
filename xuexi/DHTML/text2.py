

# 导入webdriver
from selenium import webdriver
import time
# 操作键盘按键
from selenium.webdriver.common.keys import Keys


# 创建浏览器对象   若没加入到环境变量，需要executable_path=指定PhantomJS路径
driver = webdriver.PhantomJS()

# get 方法　　selenium不区分post和get，都用get，当做图片处理
driver.get("http://www.baidu.com")
driver.maximize_window()  # 浏览器窗口等于屏幕大小
# 生成当前页面快照并保存
# driver.save_screenshot('/home/tlxy/tulingxueyuan/xuexi/DHTML/img/index.png')

# print(driver.title)

# 模拟百度搜索
# id = 'kw' 输入　美女　
driver.find_element_by_id('kw').send_keys(u'美女')
# u 中文变unk编码
# driver.find_element_by_id('kw').send_keys(Keys.RETURN)
# id = 'su' 点击搜索
driver.find_element_by_id('su').click()   # 点击失败，是默认窗口太小了，所以加driver.maximize_window()

time.sleep(2)

# driver.save_screenshot('girl.png')

# 打印当前页面源码
# print(driver.page_source)

# 打印当前页面cookie信息
# print(driver.get_cookies())

# 获取当前url
# print(driver.current_url)

# 退出
# driver.quit()