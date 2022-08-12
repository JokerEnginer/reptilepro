import requests
from bs4 import BeautifulSoup


url = 'http://www.netbian.com/qiche'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

resp = requests.get(url,headers=header)
resp.encoding='gbk'
# 将网页源代码交给bs4处理
bstext = BeautifulSoup(resp.text,'html.parser')
# 找到所有的img标签,返回一个列表
blist = bstext.find('div',class_='list').find_all('img')
# print(blist)

for iurl in blist:
    imgsrc = iurl.get('src')
    # print(imgsrc)
    img_resp = requests.get(imgsrc,headers=header)
    imgname = imgsrc.split('/')[-1]
    # print(img)
    # 图片下载
    with open('img/'+imgname,'wb') as f:
        f.write(img_resp.content)
    print('over', imgname)
resp.close()
print('all over')

