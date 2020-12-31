from urllib import request, parse

if __name__ == '__main__':

    url = 'https://www.baidu.com/s?'
    wd = input("Input your keyword:")

    # 使用data,要使用字典结构
    qs = {
        "wd": wd
    }
    print(qs)
    # 转换url编码
    qs = parse.urlencode(qs)

    fullurl = url + qs
    print(fullurl)

    rsp = request.urlopen(fullurl)
    html = rsp.read()

    # 使用get取值保证不会出错
    html = html.decode()
    # print(html)