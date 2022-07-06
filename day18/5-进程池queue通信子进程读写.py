# 作者：coding ur life
# 2022年06月20日21时42分47秒
import time
from multiprocessing import Pool, Manager
from multiprocessing import Queue
import os
# 进程池中使用queue，必须用manage().queue()
def read(q:Queue):
    print('read开始启动(%s), 父进程(%s)' % (os.getpid(), os.getpid()))
    for i in range(q.qsize()):
        print('read 在进程池读到了: %s' % q.get(True))
def write(q:Queue):
    print('write开始启动(%s), 父进程(%s)' % (os.getpid(), os.getpid()))
    for i in 'helloword':
        q.put(i)
    time.sleep(0.5)
if __name__ == '__main__':
    print('%s 开始启动' % os.getpid())
    q = Manager().Queue()
    po = Pool()
    po.apply_async(write, (q,))
    time.sleep(1)
    po.apply_async(read, (q,))
    po.close()
    po.join()
    print('%s end' % os.getpid())
