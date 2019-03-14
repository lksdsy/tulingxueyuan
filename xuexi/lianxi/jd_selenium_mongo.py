import pymongo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.PhantomJS()

wait = WebDriverWait(browser,10)

# 连接数据库 mongodb://root:ddd123@10.0.2.15:27017
client = pymongo.MongoClient('mongodb://root:ddd123@10.0.2.15:27017')
db = client.jd_computer
collection = db.computer

# 插入数据
def to_mongodb(data):
    try:
        collection.insert(data)
        print('gogogoogogogogogogo')
    except:
        print('失败了')

def seach():
    browser.get('https://www.jd.com/')
    browser.maximize_window()
    try:
        inputs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#key")))
        buttons = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#search > div > div.form > button")))
        inputs[0].clear()
        inputs[0].send_keys("笔记本")
        buttons.click()

        # 点击笔记本和销量
        button1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_selector > div:nth-child(2) > div > div.sl-value > div.sl-v-list > ul > li:nth-child(1) > a")))
        button1.click()
        button2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_filter > div.f-line.top > div.f-sort > a:nth-child(2)")))
        button2.click()

        # 获取总页数
        page = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#J_bottomPage > span.p-skip > em:nth-child(1) > b")))
        print(page[0].text)



    except TimeoutException:
        seach()

seach()