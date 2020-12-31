# 设置代理服务器
# www.xicidaili.com, www.goubanjia.com
from urllib import request, error, parse
import json

if __name__ == "__main__":
    url = "https://manage.hezongyy.com"

    proxy = {'http': '39.100.140.105:80'}
    proxy_handle = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_handle)
    request.install_opener(opener)

    try:
        rsp = request.Request(url)
        rsp.add_header("User-Agent", "1231")

        print(html)
    except error.URLError as e:
        print(e)


