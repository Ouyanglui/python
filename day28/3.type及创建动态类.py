# 作者：coding ur life
# 2022年06月30日22时37分17秒
class ObjectCreator(object):
    pass
print(type(1))  # <class 'int'>
print(type('1'))  # <class 'str'>
print(type(ObjectCreator()))  # <class '__main__.ObjectCreator'>
print(type(ObjectCreator))   # <class 'type'>


Test= type('Test', (), {'bar': True})  # 定义一个动态类Test
print(Test)  # <class '__main__.Test'>
print(Test.bar)
T = Test()  # 创建实例对象
print(T)
print(T.bar)
print(hasattr(Test, 'Foo'))  # 判断Test中是否有Foo的属性

def echo_bar(self):
    print(self.bar)

TestChild = type('TestChild', (Test,), {'echn_bar': echo_bar})  # TestChild 继承父类Test
print(TestChild)  # <class '__main__.TestChild'>
print(TestChild.bar)  # True
print(hasattr(Test, 'echo_bar'))  # False
print(hasattr(TestChild, 'bar'))  # True
