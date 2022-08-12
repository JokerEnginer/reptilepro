import re
"""
# findall()匹配字符串中所有符合正则的内容,返回的是列表
list1 = re.findall(r'\d+','我的手机号18373062,她的手机号18278369')
print(list1)

# finditer()匹配字符串中所有符合的正则内容,返回的是迭代器
its = re.finditer(r'\d+','我的手机号18373062,她的手机号18278369')
for i in its:
    print(i.group())

# search()找到结果就返回,返回的是match对象,拿数据需要使用group()
s = re.search(r'\d+','我的手机号18373062,她的手机号18278369')
print(s.group())
print('-'*30)
# match从头开始匹配
s2 = re.match(r'\d+','18373062,她的手机号18278369')
print(s2.group())
"""
"""
# 正则表达式预加载
obj = re.compile('\d+')
res = obj.findall('我的手机号18373062,她的手机号18278369')
print(res)
"""

s = """
<div class='j1'><span id='1'>大聪明</span></div>
<div class='j2'><span id='2'>大傻逼</span></div>
<div class='j3'><span id='3'>老六</span></div>
<div class='j4'><span id='4'>i坤</span></div>
<div class='j5'><span id='5'>鸡你太美</span></div>
"""
# re.S 可以让正则表达式匹配换行符
obj = re.compile(r"<div class='(?P<class>\w+?)'><span id='(?P<id>\d+)'>(?P<hh>.*?)</span></div>", re.S)
res = obj.finditer(s)
for i in res:
    print(i.group('hh'))