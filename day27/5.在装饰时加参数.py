# 作者：coding ur life
# 2022年06月29日17时45分29秒
# 装饰器携带参数时，可在原装饰器基础上设置外部变量
import time
def set_func(pre=' '):
    print('----开始装饰----')
    def call_func(func):
        print('----第二层装饰----')
        def recall_func():
            print('{} called at {} --{}'.format(func.__name__, time.ctime(), pre))
            return func()
        return  recall_func
    return call_func

@set_func('The Earth')
def test():
    print('----just a test----')

@set_func('The Moon')
def test1():
    print('----just a test1----')
test()  # test() == set_func("The Earth")test()
test1()


