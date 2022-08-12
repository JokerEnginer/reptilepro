from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

web_driver =Chrome()


web_driver.get('https://www.lagou.com')
# 找到全国的元素,并且点击
element = web_driver.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a')
element.click()
# web_driver.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a').click()
# 找到搜索框,然后输入,最后回车搜素
web_driver.find_element(By.XPATH,'//*[@id="search_input"]').send_keys('python', Keys.ENTER)

divs = web_driver.find_elements(By.XPATH,'//*[@id="jobList"]/div[1]/div')

for div in divs:
    jname = div.find_element(By.XPATH,'./div[1]/div[1]/div[1]/a').text
    cname = div.find_element(By.XPATH,'./div[1]/div[2]/div[1]/a').text
    price = div.find_element(By.XPATH,'./div[1]/div[1]/div[2]/span').text
    print(cname, jname, price)