import re
# 输入输出

name = input('your name:')
gender = input('you are a boy?(y/n)')

welcome_str = 'Welcome to the matrix {prefix} {name}.'
welcome_dic = {
    'prefix': 'Mr.' if gender == 'y' else 'Mrs',
    'name': name
}

print('authorizing...')
print(welcome_str.format(**welcome_dic))  # 双星号取出字典里的值，单星号取出list\tuple中的值


# print函数接受字符串、数字、字典、list等，input只接受字符串
a = input()
b = input()

print('a + b = {}'.format(a + b))

print('type of a is {}, type of b is {}'.format(type(a), type(b)))

print('a + b = {}'.format(int(a) + int(b)))

# JSON序列化与实战
# json的转换
import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

params_str = json.dumps(params)
print(type(params))
print(type(params_str))
original_params = json.loads(params_str)
print(type(original_params))

# JSON写入文件
with open('params.json', 'w') as p:
    json.dump(params, p)

with open('params.json', 'r') as par:
    text = par.read()
    print(text)


