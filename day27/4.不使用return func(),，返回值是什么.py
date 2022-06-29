# 作者：coding ur life
# 2022年06月29日17时35分02秒
import time
def set_func(func):
    print('----开始装饰----')
    def call_func():
        print('{} called at {}'.format(func.__name__, time.ctime()))
        return func()
    return  call_func

@set_func
def test():
    print('----Just a test----')
    return 'hahaha'  # 如果装饰器不返回func()时，这一句字符串就打不出来
print(test())

