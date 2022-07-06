# 作者：coding ur life
# 2022年06月20日21时11分26秒
from multiprocessing.pool import Pool
import time,os,random
def worker(msg): # msg:任务
    t_start = time.time()
    print('%s 开始执行，进程为 %d' % (msg, os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,' 执行完毕,耗时%0.2fs' % (t_stop-t_start))
if __name__ == '__main__':
    po = Pool()  # 默认为全部进程都接到任务后才开始结束任务
    for i in range(10):
        po.apply_async(worker, (i,))
    print('-----start-----')
    po.close()
    po.join()
    print('-----end-----')