from selenium.webdriver import Chrome
# 创建浏览器对象
webdriver =Chrome()
webdriver.get('http://www.baidu.com')
print(webdriver.title)
