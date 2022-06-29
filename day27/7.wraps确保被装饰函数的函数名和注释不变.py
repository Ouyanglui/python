# 作者：coding ur life
# 2022年06月29日18时14分55秒
import time
from functools import wraps
def set_func(func):
    print('----开始装饰----')
    @wraps(func)
    def call_func():
        print('{} called at {}'.format(func.__name__, time.ctime()))
        return func
    return call_func
@set_func
def test():
    '''保持原来的名字不变'''
    print('---a test---')
test()
print(test.__name__, test.__doc__)
