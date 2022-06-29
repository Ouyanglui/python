# 作者：coding ur life
# 2022年06月29日18时07分29秒
class Test:
    def __init__(self, func):
        self.func = func
        # 装饰时需要的操作写进init里(外部函数和闭包之间的操作)
    def __call__(self, *args, **kwargs):  # 装饰前（执行）需要的操作写进call里
        print('----this is a validation----')
        return self.func(*args, **kwargs)


@Test
def test():
    print('----a test----')
test()
# ----this is a validation----
# ----a test---