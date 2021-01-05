# 字符
s1 = 'hello'
s2 = "hello"
s3 = """hello"""
print(s1 == s2 == s3)

# 内嵌
print("I'm a student")

# python字符串不可改变， '+='是个例
s = 'hello'
s[2] = '3'
# 通过创建新的字符串实现
s = 'H' + s[1:]
print(s)
s = s.replace('H', 'h')
print(s)

# 内置函数join
l = []
for n in range(0, 100000):
    l.append(str(n))
l = ' '.join(l)
print(type(l))

# 内置函数split
def query_data(namespace, table):
    """
    given namespace and table, query database to get corresponding
    data
    """

path = 'hive://ads/training_table'
namespace = path.split('//')[1].split('/')[0] # 返回'ads'
print(namespace)
table = path.split('//')[1].split('/')[1] # 返回 'training_table'
print(table)
data = query_data(namespace, table)

# 常用函数
# string.strip(str)，表示去掉首尾的 str 字符串
# string.lstrip(str)表示只去掉开头的 str 字符串
# string.rstrip(str)，表示只去掉尾部的 str 字符串

