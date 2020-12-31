# 服务器通过UserAgent判断访问者身份
from urllib import request, error

if __name__ == "__main__":
    url = "https://www.baidu.com/"

    try:
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
        # 两种带入headers信息的方式
        # req = request.Request(url, headers=headers)
        req = request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0")

        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(type(html))
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)


