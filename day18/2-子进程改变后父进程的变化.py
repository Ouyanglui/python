# 作者：coding ur life
# 2022年06月20日19时16分46秒
from multiprocessing import Process
import os
import time
# def run_proc(*args, **kwargs):
#     for i in range(10):
#         print('子进程进行中,name = %s,age = %d pid=%d...' % (args[0], args[1], os.getpid()))
#         print(args)
#         print(kwargs)
#         time.sleep(0.2)
#
#
# if __name__ == '__main__':
#     p = Process(target=run_proc, args=('lily', 20), kwargs={'m': 3})  # 传参
#     p.start()

nums = [10, 11]
def work1():
    for i in range(3):
        nums.append(i)
        print('p1进程 pid=%d, nums=%s' % (os.getpid(), nums))
    # for i in range(3):
    #     nums.append(i)
    time.sleep(0.5)
def work2():
    print('p2进程 pid=%d, nums=%s' % (os.getpid(), nums))
if __name__ == '__main__':
    p1 = Process(target=work1)
    p1.start()
    p1.join()
    # 子进程全局变量不影响父进程，因为父进程是影分身出子进程
    p2 = Process(target=work2)
    p2.start()