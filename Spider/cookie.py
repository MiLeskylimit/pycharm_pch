from urllib import request, parse
from http import cookiejar

# 手动添加Cookie爬取人人网信息
if __name__ == "__main__":
    url = "http://www.renren.com/975574809/profile"
    header = {
        "Cookie": "anonymid=kj3v6xb3-yx6kir; depovince=GW; jebecookies=01c17f37-6025-4e89-b446-316321aa60cc|||||; _r01_=1; ick_login=734c5dae-38d6-4f14-a00e-db7de28a4201; taihe_bi_sdk_uid=a7ce812ff10bc9cafe5587cb8481ff20; taihe_bi_sdk_session=97f1e45a924c933dc58b562eced0d5f1; t=9ee343e09cc8cc5f1904ee94b6a232c59; societyguester=9ee343e09cc8cc5f1904ee94b6a232c59; id=975574809; xnsid=6785476b; ver=7.0; loginfrom=null; wp_fold=0"
    }
    rsp = request.Request(url, headers=header)
    rsp = request.urlopen(rsp)
    html = rsp.read().decode()

    with open("rsp.html", "w", encoding="utf-8") as f:
        f.write(html)

