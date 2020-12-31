# -*- coding: utf-8 -*-
# list和tuple
from timeit import *

# tuple
tup = (1, 2, 3, 4)
# 元组只有重新创建才能改变元素
new_tup = tup + (5,)
print(new_tup)

# list
l = [1, 2, 3, 4]
# 列表可以在原有基础上改变
l.append(5)
print(l)

# 列表和元组支持副索引
print(tup[-1])
print(l[-1])

# 列表和元组都支持切片
print(tup[1:3])
print(l[1:3])

# 列表和元组可以随意嵌套
tup = ((1, 2, 3), (4, 5, 6))
l = [[1, 2, 3], [4, 5]]

# 列表和元组可以随意转换
print(type(tup))
print(type(l))
print(type(list(tup)))
print(type(tuple(l)))

# 列表和元组的内置函数
l = [3, 2, 3, 5, 6, 3, 9]
print(l.count(3))   # 统计元素出现的次数
print(l.index(3))   # 查看元素第一次出现的索引
l.reverse()         # 反转列表
print(l)
l.sort()            # 列表排序
print(l)
tup = (3, 2, 3, 5, 6, 3, 9)
print(tup.count(3))
print(tup.index(9))
print(type(tup))
a = list(reversed(tup))   # 元组无法直接操作，只能转换为列表反转
print(a)
b = sorted(tup)           # 元组排序后为列表
print(type(b))

# 存储差异-列表比元组需要更多的空间存储索引
l = [1, 2, 3]
print(l.__sizeof__())
tup = (1, 2, 3)
print(tup.__sizeof__())

# 对比创建列表方法的效率
print(timeit('l = list()'))
print(timeit('l = []'))
