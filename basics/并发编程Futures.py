# coding=utf-8
# 下载网站内容并打印
import requests
import time

def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))

def download_all(sites):
    for site in sites:
        download_one(site)

def main():
    sites = [
        'http://docs.kubernetes.org.cn/227.html',
        'http://docs.kubernetes.org.cn/247.html',
        'http://docs.kubernetes.org.cn/246.html',
        'http://docs.kubernetes.org.cn/248.html',
        'http://docs.kubernetes.org.cn/249.html',
        'http://docs.kubernetes.org.cn/250.html',
        'http://docs.kubernetes.org.cn/251.html',
        'http://docs.kubernetes.org.cn/252.html',
        'http://docs.kubernetes.org.cn/',
        'http://docs.kubernetes.org.cn/227.html#Kubernetes-2'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

if __name__ == '__main__':
    main()

# Futures 使用
import concurrent.futures
import requests
import threading
import time

def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))

def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_one, sites)  # 遍历sites，并分别传给download_one调用

def main():
    sites = [
        'http://docs.kubernetes.org.cn/227.html',
        'http://docs.kubernetes.org.cn/247.html',
        'http://docs.kubernetes.org.cn/246.html',
        'http://docs.kubernetes.org.cn/248.html',
        'http://docs.kubernetes.org.cn/249.html',
        'http://docs.kubernetes.org.cn/250.html',
        'http://docs.kubernetes.org.cn/251.html',
        'http://docs.kubernetes.org.cn/252.html',
        'http://docs.kubernetes.org.cn/',
        'http://docs.kubernetes.org.cn/227.html#Kubernetes-2'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

if __name__ == '__main__':
    main()


# Futures 进阶用法
import concurrent.futures
import requests
import time

def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))

def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do = []
        for site in sites:
            future = executor.submit(download_one, site)
            to_do.append(future)

        for future in concurrent.futures.as_completed(to_do):
            future.result()

def main():
    sites = [
        'http://docs.kubernetes.org.cn/227.html',
        'http://docs.kubernetes.org.cn/247.html',
        'http://docs.kubernetes.org.cn/246.html',
        'http://docs.kubernetes.org.cn/248.html',
        'http://docs.kubernetes.org.cn/249.html',
        # 'https://en.wikipedia.org/wiki/Portal:The_arts',
        'http://docs.kubernetes.org.cn/251.html',
        'http://docs.kubernetes.org.cn/252.html',
        'http://docs.kubernetes.org.cn/',
        'http://docs.kubernetes.org.cn/227.html#Kubernetes-2'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

if __name__ == '__main__':
    main()


