# 1
def a_ml(func):
    def b_ml(*args, **kwargs):
        print('11212')
        func(*args, **kwargs)
    return b_ml

@a_ml
def c_ml():
    print('32323')

# c_ml = a_ml(c_ml)
c_ml()

# 2   元信息的保留 @ functools.wraps()
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)

    return wrapper

@my_decorator
def greet(message):
    print(message)

print(greet.__name__)

# 计算函数的运行时间
import time
import functools

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 1000))
        return res

    return wrapper

@log_execution_time
def calculate_similarity(items):
    pass

# 输入合理性检测
def validation_check(input):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ...  # 检查输入是否合法

@validation_check
def neural_network_training(param1, param2, ...):
    ...

# 缓存 @lru_cache
@lru_cache
def check(param1, param2, ...) # 检查用户设备类型，版本号等等
    ...



