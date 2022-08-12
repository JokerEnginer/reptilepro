import requests

query = input("请输入需要查询的任务")
url = f'https://www.sogou.com/web?query={query}'
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
resp = requests.get(url,headers = header)
print(resp)
print(resp.text)