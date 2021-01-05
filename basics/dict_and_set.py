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
d = {'name': 'jason', 'age': 20}
d['addr'] = '南礼士路37号'
d.pop('name')
print(d)

# 集合中的元素
s = {1, 2, 3}
s.add(4)  # 增加元素4到集合
print(s)
s.remove(3)  # 从集合中删除元素4
print(s)

# 字典的排序
d = {'b':1, 'a':2, 'c':10}
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0])
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1])
print(d_sorted_by_key)
print(d_sorted_by_value)

# 集合的排序
s = {3, 5, 2, 10}
sorted(s)

# 字典和集合的性能
#    例子1
# list存储商品id、名称、价格，更具id找价格
def find_product_price(products, product_id):
    for id, price in products:
        if id == product_id:
            return price
    return None
#  list
# products = [
#     (1421231, 100),
#     (394385994, 30),
#     (293923, 150)
# ]
# print('The price of product 1421231 is {}'.format(find_product_price(products, 1421231)))

# dict
products = {
    1421231: 100,
    394385994: 30,
    293923: 150
}
print('The price of product 1421231 is {}'.format(products[1421231]))

#   例子2
import time
id = [x for x in range(0, 100000)]
price = [x for x in range(200000, 300000)]
products = list(zip(id, price))

# list version
def find_unique_price_using_list(products):
    unique_price_list = []
    for _, price in products:
        if price not in unique_price_list:
            unique_price_list.append(price)
    return len(unique_price_list)

# set version
def find_unique_price_using_set(products):
    unique_price_set = set()
    for _, price in products:
        unique_price_set.add(price)
    return len(unique_price_set)

# 计算列表版本的时间
start_using_list = time.perf_counter()
find_unique_price_using_list(products)
end_using_list = time.perf_counter()

print("time elapse using list: {}".format(end_using_list - start_using_list))

# 计算集合版本的时间
start_using_set = time.perf_counter()
find_unique_price_using_set(products)
end_using_set = time.perf_counter()

print("time elapse using set: {}".format(end_using_set - start_using_set))


# 题目1
d = {'name': 'jason', ['education']: ['Tsinghua University', 'Stanford University']}







