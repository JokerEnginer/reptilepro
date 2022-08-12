import requests

url = 'https://fanyi.baidu.com/sug'

keyword = input('请输入需要查询的英文:')

data = {'kw':keyword}
# 发送post请求,发送的数据需要放在字典中,通过data参数进行传递
resp = requests.post(url,data=data)
print(resp.json()) # 将服务器返回的内容直接处理成json()