import requests


url = 'https://movie.douban.com/j/new_search_subjects'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

pars = {
    'sort': 'U',
    'range': '0,10',
    'tags':'',
    'start': 0,
    'genres': '喜剧'
}
resp = requests.get(url,params=pars,headers=header)
print(resp.json())


