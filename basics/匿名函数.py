# lambda
a = lambda b: b**3
print(a(3))

c = [(lambda x: x*x)(x) for x in range(10)]
print(c)

# lambda用作函数的参数
l = [(1, 20), (3, 0), (9, 10), (2, -1)]
l.sort(key=lambda x: x[1])    # 按列表中元组的第二个元素排序
print(l)


def multiply_2(l):
    f = []
    for i in l:
        f.append(i * 2)
    return f

l = [1, 2, 3, 4]
print(multiply_2(l))
print(multiply_2(l))
print(multiply_2(l))

# map函数把iterable对象中的每个元素传入function
l = [1, 2, 3, 5, 0]
a = list(map(lambda x: x * 2, l))
print(a)

# filter 返回function结果为true的结果
l = [1, 2, 3, 4, 5]
new_list = list(filter(lambda x: x % 2 == 0, l))
print(new_list)

# reduce function接受两个参数 上次调用的结果和iterable中的元素
from functools import reduce
l = [1, 2, 3]
product = reduce(lambda x, y: x * y, l)
print(product)

# 对一个字典的值进行排序
d = {'mike': 10, 'lucy': 2, 'ben': 30}
d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print(d)


