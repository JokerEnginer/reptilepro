import requests
from lxml import etree
import csv
url = 'https://shenzhen.zbj.com/search/service/?kw=saas&r=1'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

resp = requests.get(url, headers=header)
resp.encoding='utf-8'
# print(resp.text)
tree = etree.HTML(resp.text)
divs = tree.xpath('//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div')
f = open(r'E:\djangostudy\reptilepro\day3\pig.csv', 'w',encoding='utf-8')
csvf = csv.writer(f)
for div in divs:
     price = div.xpath('./div[3]/div[1]/span/text()')
     title = div.xpath('./div[3]/a/text()')
     m = price+title
     csvf.writerow(m)
f.close()
resp.close()