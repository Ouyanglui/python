# 作者：coding ur life
# 2022年06月29日16时28分17秒
import time
def set_func(test):
    print('----开始装饰1----')
    def call_func():
        start_time = time.time()
        test()
        stop_time = time.time()
        print('all time is {}'.format(stop_time - start_time))
    return call_func

def set1_func(test):
    print('----开始装饰2----')
    def call1_func():
        print('{} called is at {}'.format(test.__name__, time.ctime()))
        test()
    return call1_func
@set1_func
@set_func
def test1():
    print('----Just is a test----')
    for i in range(10000):
        pass

test1()
