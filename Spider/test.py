from selenium import webdriver
import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import os,pytz,requests,time,lxml,lxml.html
import requests
import json

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chromedriver = "/usr/bin/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)

# driver.get('http://bpo.gcheck.com.cn:8088/#/attendance/myattendance')
# driver.find_element_by_xpath('/html/body/section/form/div[2]/div/div[1]/input').send_keys("P0169311")
# driver.find_element_by_xpath('/html/body/section/form/div[3]/div/div[1]/input').send_keys("123456")
# driver.find_element_by_xpath('/html/body/section/form/div[4]/div/div/input').send_keys("746")

# driver.find_element_by_xpath("/html/body/section/form/button").click()
# driver.find_element_by_xpath('//*[@id="main"]/section/section/section[2]/div/div[1]/div/ul/section/section/article/p').click()

# driver.quit()

# msg = '测试消息'
# wxpushplus = 'http://www.pushplus.plus/send?token=a767222b76fa42bfa3ba8fc93673f6ed&title={}&content={}&template=markdown'
# requests.post(wxpushplus.format(msg , str(datetime.datetime.now(pytz.timezone('Asia/Shanghai'))) + ' 公司打卡状态: ' + msg))
# print(str(datetime.datetime.now(pytz.timezone('Asia/Shanghai'))) + ' 公司打卡状态: ' + msg)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)

driver.get('http://bpo.gcheck.com.cn:8088/#/attendance/myattendance')
time.sleep(3)
driver.find_element_by_xpath('/html/body/section/form/div[2]/div/div[1]/input').send_keys("P0169311")
driver.find_element_by_xpath('/html/body/section/form/div[3]/div/div[1]/input').send_keys("123456")
driver.find_element_by_xpath('/html/body/section/form/div[4]/div/div/input').send_keys("746")
driver.find_element_by_xpath("/html/body/section/form/button").click()
time.sleep(2)
# driver.find_element_by_xpath('//*[@id="main"]/section/section/section[2]/div/div[1]/div/ul/section/section/article/p').click()
# try:
# #   driver.find_element_by_link_text('打卡').click()
# #   driver.find_element_by_css_selector('#main > section > section > section.app-wrapper > div > div.scrollbar-wrapper.el-scrollbar__wrap > div > ul > section > section > article > p')
# except:
#    print('跳过了异常')
# else:
#    print('没有异常')
   
try:
  text = driver.find_element_by_xpath('//*[@id="main"]/section/section/section[2]/section/section[1]/section/div[1]/div[3]/div[3]/table/tbody/tr[1]').text 
  print(text)
except:
  print('catch a bug')
else:
  print('没有异常')

# htmls = driver.page_source
# WebDriverWait(driver, 10)
# print(htmls)
# html = lxml.html.fromstring(htmls)
# print(html)
# # items = html.xpath('//*[@id="main"]/section/section/section[2]/section/section[1]/section/div[1]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td[1]')
# items = html.xpath('//*[@id="main"]/section/section/section[2]/section/section[1]/section/div[1]/div[3]/div[4]/div[2]/table/tbody')
# print(items)


## screen shot
# driver.save_screenshot('./1.png') 

driver.get_screenshot_as_file("./1.png")


driver.quit()
## upload pic

headers = {'Authorization': 'QgL9qIAkqfrRjkezWs4RvM4NekDjIzcm'}
files = {'smfile': open('./1.png', 'rb')}
url = 'https://sm.ms/api/v2/upload'
res = requests.post(url, files=files, headers=headers).json()
purl = res['data']['url']
url = '<img src="{}">'.format(purl)



## send  msg
msg = '签到消息'
print(url)
wxpushplus = 'http://www.pushplus.plus/send?token=a767222b76fa42bfa3ba8fc93673f6ed&title={}&content={}&template=html'
requests.post(wxpushplus.format(msg , str(datetime.datetime.now(pytz.timezone('Asia/Shanghai'))) + ' 公司打卡状态: ' + url))
print(str(datetime.datetime.now(pytz.timezone('Asia/Shanghai'))) + ' 公司打卡状态: ' + msg)



