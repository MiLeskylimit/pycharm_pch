# 迭代器
# 可迭代对象通过.iter函数返回一个迭代器，通过next()函数遍历

def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False

params = [
    1234,
    '1234',
    [1, 2, 3, 4],
    set([1, 2, 3, 4]),
    {1: 1, 2: 2, 3: 3, 4: 4},
    (1, 2, 3, 4)
]

for param in params:
    print('{} is iterable? {}'.format(param, is_iterable(param)))

# 生成器
# 迭代器枚举元素需要事先生成元素
generator = (i for i in range(1000))
# 此处i in range(1000)相当于
while True:
    val = next(range(1000))
    if val == i:
        yield True
