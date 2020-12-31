import chardet
from urllib import request

if __name__ == "__main__":
    url = 'https://baijiahao.baidu.com/s?id=1686731601925002129&wfr=spider&for=pc'
    rsp = request.urlopen(url)

    print(type(rsp))

    print("URL: {0}".format(rsp.geturl()))
    print("Info: {0}".format(rsp.info()))
    print("Code: {0}".format(rsp.getcode()))

    # html = rsp.read()
    # cs = chardet.detect(html)
    # print(type(cs))
    # print(cs)
    # html = html.decode(cs.get("encoding", "utf-8"))
    # print(html)