# 找出list中最大的值
def find_largest_element(l):
    if not isinstance(l, list):
        print('input is not type of list')
        return
    if len(l) == 0:
        print('empty input')
        return
    largest_element = l[0]
    for item in l:
        #print(item)
        if item > largest_element:
            largest_element = item
            #print(largest_element)
    print('largest element is: {}'.format(largest_element))

find_largest_element([1, 3, 4, 5, 0])

# 合理使用函数嵌套
def factorial(input):
    # validation check
    if not isinstance(input, int):
        raise Exception('input must be an integer.')
    if input < 0:
        raise Exception('input must be greater or equal to 0' )

    def inner_factorial(input):
        #print(input)
        if input <= 1:
            return 1
        return input * inner_factorial(input-1)
    return inner_factorial(input)

print(factorial(5))

# 变量的作用域
MIN_VALUE = 1
MAX_VALUE = 10
def validation_check(value):
    # global声明此处变量就是全局变量
    global MIN_VALUE
    MIN_VALUE += 1
    print(MIN_VALUE)
validation_check(5)

def validation_check(value):
    # 变量相同的情况会覆盖全局变量
    MIN_VALUE = 4
    print(MIN_VALUE)
validation_check(5)

# 嵌套函数变量通过nonlocal声明，不加则会覆盖
def outer():
    x = "local"
    def inner():
        nonlocal x  # nonlocal关键字表示这里的x就是外部函数outer定义的变量x
        x = 'nonlocal'
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

# 闭包
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of  # 返回值是exponent_of函数

square = nth_power(2)      # 计算一个数的平方
cube = nth_power(3)    # 计算一个数的立方
print(type(square))

print(square(2))  # 计算2的平方
print(cube(2))  # 计算2的立方


def check_str(values):
    if not isinstance(values, int):
        print("类型错误")
    print(values)

check_str(12)
check_str("age")

print("类型错误")


# 函数嵌套的调用和顺序没关
def sin():
    return sin

def sin_f(a=sin(3)):
    b = a*10
    return b
print(sin_f())