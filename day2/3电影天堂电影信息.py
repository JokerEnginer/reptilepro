import re
import requests

main_url = 'https://www.dy2018.com/'
header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
resp = requests.get(main_url,headers=header)
resp.encoding='gb2312'
main_text = resp.text
main_obj = re.compile(r'2022必看热片.*?<ul>(?P<movies>.*?)</ul>',re.S)
child_obj = re.compile(r"<a href='(?P<child>.*?)'", re.S)
download_obj = re.compile(r'<h1>(?P<mname>.*?)</h1>.*?'
                          r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf">'
                          r'<a href="(?P<download>.*?)">.*?</a></td>',re.S)
its = main_obj.finditer(main_text)
child_url_list = []
for it in its:
    uls = it.group('movies')
    result = child_obj.finditer(uls)
    for itt in result:
        # print(itt.group('child'))
        child_href = main_url+itt.group('child').strip('/')
        child_url_list.append(child_href)

# 获取子页面的信息
for href in child_url_list:
    child_resp = requests.get(href, headers=header)
    child_resp.encoding='gb2312'
    child_context = child_resp.text
    respms = download_obj.search(child_context)
    print(respms.group('mname'))
    print(respms.group('download'))
