from urllib import request, parse
from http import cookiejar



def login():

    url = 'https://newapi.hezongyy.com/users/UserLogin/login'
    datas = {"username": "测试05", "password": "a123456"}
    data1 = parse.urlencode(datas)
    print(data1)
    print(type(data1))


if __name__ == "__main__":
    login()











