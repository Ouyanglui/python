# 作者：coding ur life
# 2022年06月30日21时55分00秒
def choose_class(name):
    if name == "foo":
        class Foo:
            pass
        return Foo
    else:
        class Bar:
            pass
        return Bar
my_class = choose_class('foo')
print(my_class)  # <class '__main__.choose_class.<locals>.Foo'>
my_class = choose_class('bar')
print(my_class)  # <class '__main__.choose_class.<locals>.Bar'>