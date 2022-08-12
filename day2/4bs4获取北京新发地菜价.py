from bs4 import BeautifulSoup
import requests

main_url = 'http://www.xinfadi.com.cn/getPriceData.html'
header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

data = {
    'limit':'',
    'current':'',
    'pubDateStartTime':'',
    'pubDateEndTime':'',
    'prodPcatid':'',
    'prodCatid':'',
    'prodName':'',
}
# 数据解析,将页面源代码交给BeautifulSoup进行处理,生成bs对象
resp = requests.post(main_url, data=data, headers=header)
# resp = requests.post(main_url, params=data, headers=header)
# bstext = BeautifulSoup(resp.text,'html.parser')  # 指定html解析器
jsontext = resp.json()
for i in jsontext.items():
    print(i)
resp.close()


