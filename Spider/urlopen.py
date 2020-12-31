from urllib import request

# 使用urllib.reques请求一个网页内容

if __name__ == '__main__':

    url = "https://www.aliyun.com/?utm_content=se_1007692031&accounttraceid=43569a8727ad4a2890c1cd2904fa4b50nwju"
    rsp = request.urlopen(url)
    # 打印返回结果
    html = rsp.read()
    # 直接读出来为bytes类型
    print(type(html))
    # 解码-转换成str
    html = html.decode()
    # 类型查看
    print(type(html))
    # print(html)
