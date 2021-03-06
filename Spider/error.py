# URL——error使用
from urllib import error, request

if __name__ == "__main__":
    url = "https://www.baidu.com/fea.html"
    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print("HTTPError: {0}".format(e.reason))
    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))
    except Exception as e:
        print(e)
