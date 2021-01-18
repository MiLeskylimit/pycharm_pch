import time
import asyncio

def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))

def main(urls):
    for url in urls:
        crawl_page(url)

# 普通调用
# main(['url_1', 'url_2', 'url_3', 'url_4'])

# 协程调用
# asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))

async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        await task

asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
0