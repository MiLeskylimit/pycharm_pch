# 对象的拷贝，比较
# 事实上，出于对性能优化的考虑，Python 内部会对 -5 到 256 的整型维持一个数组，起到一个缓存的作用。这样，每次你试图创建一个 -5 到 256 范围内的整型数字时，Python 都会从这个数组中返回相对应的引用，而不是重新开辟一块新的内存空间。但是，如果整型数字超过了这个范围，比如上述例子中的 257，Python 则

a = 257
b = 257

if a == b:
    print("true")
else:
    print("False")

if a is b:
    print("true")
else:
    print("False")
