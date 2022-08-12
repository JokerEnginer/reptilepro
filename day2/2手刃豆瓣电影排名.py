import re
import requests
import csv
url = 'https://movie.douban.com/chart'
header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
resp = requests.get(url,headers=header)
# 获取页面代码
page_context = resp.text

obj = re.compile(r'<div class="">.*?<span style="font-size:13px;">(?P<title>.*?)</span>.*?<span class="rating_nums">(?P<score>.*?)</span><span class="pl">((?P<num>.*?)人评价)</span>', re.S)

result = obj.finditer(page_context)
f = open(r'E:\djangostudy\reptilepro\day2\movies.csv','w')
csvwriter = csv.writer(f)

for i in result:
    # print(i.group('title'))
    # print(i.group('score'))
    # print(i.group('score'))
    dic = i.groupdict()
    csvwriter.writerow(dic.values())
f.close()
resp.close()