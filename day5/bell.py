# import requests
#
# url =  'https://oa.bell.ai/api/teaching/teacher/members?department_id=95&page=1&per_page=50'
#
# header = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
#     "Cookie":"Hm_lvt_7f7bca070626608ea7f92b867c9f95dc=1645350567; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217ba98b4fd97f-0b98f2cd816282-c343365-1049088-17ba98b4fdab28%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22%24device_id%22%3A%2217ba98b4fd97f-0b98f2cd816282-c343365-1049088-17ba98b4fdab28%22%7D; token=eyJhbGciOiJIUzI1NiIsImlhdCI6MTY2MDI3MTY4OCwiZXhwIjoxNjYwODc2NDg4fQ.eyJzaGFkb3ciOjAsImxvZ2luX3NvdXJjZSI6NCwiaWQiOjExOTUwLCJ1c2VyX3R5cGUiOjF9.CmrAqR_JORK4jyF0ngZJKGOgPaMr7-rjRARbH4aFDQQ; expire_time=2022/08/19 10:34:48; session=eyJvcGVuaWQiOiJvUUJXQTFGN3QweS02TjZ4LWdfeU9Yem9UTmdvIiwidW5pb25pZCI6Im9RU1c3d01qTzUwY2M1NUtGSlhzMUpKSlRQeU0iLCJ1c2VyX3R5cGUiOjF9.YvW8SA.NDCs8-cJHpeueborRdUoD2HCzVk",
#     "Referer": "https://oa.bell.ai/web.html",
# }
#
# resp = requests.get(url,headers=header,data={
#
# })
# print(resp.text)

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time


web = Chrome()
web.get('https://oa.bell.ai/')
time.sleep(1)
web.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div[1]/div/form/div[1]/div/div[1]/input').send_keys('18378330626')
web.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div[1]/div/form/div[2]/div/div[1]/input').send_keys('zsr18378330626@')
time.sleep(1)
web.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div[1]/div/div[2]/button').click()
time.sleep(1)
web.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div/ul[1]/li[3]/div/div[2]').click()
time.sleep(1)
web.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div/ul[2]/li[2]/ul[2]/li[1]/a').click()
time.sleep(1)
web.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[17]/button[1]').click()
time.sleep(1)
trs = web.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/div/div[5]/div[1]/div[3]/table/tbody/tr')
time.sleep(1)
for tr in trs:
    # '/td[2]/div/div[1]/button/span/span'
    name = tr.find_element(By.XPATH,'/td[2]/div/div[1]/button/span/span').text
    print(name)

