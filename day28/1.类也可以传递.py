# 作者：coding ur life
# 2022年06月30日21时44分49秒
class ObjectCreator(object):
    pass
def echo(obj):
    print(obj)
    obj.new_attribute = 'foo'

echo(ObjectCreator)
print(ObjectCreator.new_attribute)

