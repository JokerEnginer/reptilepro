from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
web = Chrome()
web.get('https://www.lagou.com')
web.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a').click()
time.sleep(1)
web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys('python',Keys.ENTER)
# 注意此时selenium已经打开了一个新的窗口,但是没有自动切换,还是在原有的页面中
web.find_element(By.XPATH,'//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
time.sleep(1)
# 切换到最新的页面窗口
web.switch_to.window(web.window_handles[-1])
job_detail =web.find_element(By.XPATH,'//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)

# 关闭页面
web.close()
# 回到最初的页面
web.switch_to.window(web.window_handles[0])



