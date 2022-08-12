from lxml import etree


xml = '''
    <book>
        <id>1</id>
        <name>老王</name>
        <price>老王</price>
        <price>1000</price>
        <nick>舒服的很</nick>
        <author>
            <nick id='123'>小周</nick>
            <nick id='456'>小马</nick>
            <nick class='joy'>小周</nick>
            <nick class='cai'>蔡小姐</nick>
            <div>
                <nick>喏了1</nick>
            </div>
            <div>
                <nick>喏了2</nick>
            </div>
        
        </author>
        <partner>
            <nick id='ppc'>小红</nick>
            <nick id='pbbc'>小绿</nick>
        </partner>
    </book>
'''

tree = etree.XML(xml)
# result = tree.xpath('/book')  # /表示成绩关系.第一个/表示根节点
result = tree.xpath('/book/name/text()')  # text()拿文本
result1 = tree.xpath('/book//nick/text()') # // 后代节点
result2 = tree.xpath('/book/*/nick/text()') # *任意的节点
print(result)
print(result1)
print(result2)