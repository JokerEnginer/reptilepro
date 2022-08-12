import requests


url = 'https://www.17k.com/all'
header = {"cookie":"GUID=d73311e0-945d-4012-a3a5-d42b43444a28; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22d73311e0-945d-4012-a3a5-d42b43444a28%22%2C%22%24device_id%22%3A%221827bcd45d34d7-007f8e20e4afb9-26021d51-1049088-1827bcd45d4cca%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D"}

ss = requests.session()

resp = ss.get(url,headers=header)
print(resp.text)

resp.close()
