# 作者：coding ur life
# 2022年06月29日16时57分39秒
def set_func(func):
    print('----开始装饰----')
    def call_func(*args, **kwargs):
        print('----权限验证1----')
        print('----权限验证2----')
        func(*args, **kwargs)  # 拆包
    return call_func

@set_func
def test(num, *args, **kwargs):
    print('----test----{}'.format(num))
    print('----test----', args)
    print('----test----', kwargs)
test(100)
test(100, 200)
test(100, 200, m=2)