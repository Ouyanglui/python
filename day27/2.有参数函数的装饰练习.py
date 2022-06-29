# 作者：coding ur life
# 2022年06月29日16时48分55秒
import time
def set_func(func):
    print('----开始装饰----')
    def call_func(a, b):
        print('{} called at {}'.format(func.__name__, time.ctime()))
        print(a, b)
        func(a, b)
        print(a+b)
    return call_func
@set_func  # 等价于foo = set_func(foo)
def foo(a,b):
    print('what is that?')
foo(1,2)