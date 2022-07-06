# 作者：coding ur life
# 2022年06月20日20时23分52秒

from multiprocessing import Queue, Process
import time
# q = Queue(3)  # 初始化对象，最多可接收三条信息  管道通信，FIFO 不放置时默认数量最大
# q.put('A')
# q.put('B')
# q.put('C')
# print(q.full())  # True or False
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.empty())
def write(q:Queue):
    for i in ['A', 'B', 'C']:
        print('writing')
        q.put(i)
        time.sleep(0.5)
def read(q:Queue):
    while True:
        if not q.empty():
        # 判断下管道中是否有数据
            i = q.get(True)
            print('Get %s from Queue' % i)
            time.sleep(1)
        else:
            break
if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pw.start()
    time.sleep(0.5)
    pr = Process(target=read, args=(q,))
    pr.start()
    pw.join()
    pr.join()
    print(q.qsize())
