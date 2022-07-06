# 作者：coding ur life
# 2022年06月20日17时43分18秒
# 获取进程pid
from multiprocessing import Process
import os


def run_proc():
    print('子进程运行中， pid = %d...' % os.getpid())
    print('子进程结束了')


if __name__ == '__main__':
    print('父进程pid= %d...' % os.getpid())
    p = Process(target=run_proc())
    p.start()
