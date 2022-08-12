from urllib.request import urlopen
url = 'http://www.baidu.com'
resp = urlopen(url)
with open(r"E:\djangostudy\reptilepro\day1\bu.html",'w',encoding='utf-8') as f:
    f.write(resp.read().decode('utf-8'))
print('over')