import os
from shutil import copyfile
import time

BASE_DIR = 'server/'
NET_DIR = 'net/'

def main():
    filenames = os.listdir(BASE_DIR)
    for i, filename in enumerate(filenames):
        print('copying {} into net drive... {}/{}'.format(filename, i + 1, len(filenames)))
        copyfile(BASE_DIR + filename, NET_DIR + filename)
        print('copied {} into net drive, waiting client complete... {}/{}'.format(filename, i + 1, len(filenames)))

        while os.path.exists(NET_DIR + filename):
            time.sleep(3)

    print('transferred {} into client. {}/{}'.format(filename, i + 1, len(filenames)))

if __name__ == "__main__":
main()

++++++++++++++++++++++
# 我们假设 client 电脑上要输出的文件夹在 BASR_DIR ，网盘的路径在 NET_DIR

import os
from shutil import copyfile
import time

BASE_DIR = 'client/'
NET_DIR = 'net/'

def main():
    while True:
        filenames = os.listdir(NET_DIR)
        for filename in filenames:
            print('downloading {} into local disk...'.format(filename))
            copyfile(NET_DIR + filename, BASE_DIR + filename)
            os.remove(NET_DIR + filename) # 我们需要删除这个文件，网盘会提我们同步这个操作，从而 server 知晓已完成
            print('downloaded {} into local disk.'.format(filename))
        time.sleep(3)

if __name__ == "__main__":
main()