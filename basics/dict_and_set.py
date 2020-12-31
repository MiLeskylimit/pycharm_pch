# -*- coding: utf-8 -*-
# dict and set

# 字典的创建
d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')
print(d1 == d2 == d3 == d4)
# 集合的创建
s1 = {1, 2, 3}
s2 = set([1, 2, 3])
print(s1 == s2)

# 集合和字典元素可以是混合类型
s = {1, 'hello', 5.0}

# 字典访问方式，不存在可以设置默认值
d = {'name': 'jason', 'age': 20}
# print(d['name'])
# print(d['location'],)
print(d.get('name'))
print(d.get('location', 'null'))

# 集合访问方式-不支持索引操作，本质上是一个哈希表
s = {1, 2, 3}
# s[0]

# 删除字典中的元素
d['addr'] = '南礼士路37号'
d.pop('name')
print(d)
# 删除字典、集合中的元素


