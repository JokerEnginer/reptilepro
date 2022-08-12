from lxml import etree


tree = etree.parse('index.html')

# result = tree.xpath('/html')
# result = tree.xpath('/html/body/ul/li/a/text()'
# result = tree.xpath('/html/body/ul/li[1]/a/text()')  # 使用中括号获取第几个,索引从1开始数
# result = tree.xpath('/html/body/ol/li/a[@href="feiji"]/text()') # [@]获取指定属性的文本
result = tree.xpath('/html/body/ol/li/a/@href')
print(result)

