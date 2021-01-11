# metaclass
class MyClass:
  pass

instance = MyClass()

print(type(instance))
print(type(MyClass))   # 都是type的实例

# 上列类使用type手工调用
class = type(classname, superclasses, attributedict)

# 一旦你把一个类型 MyClass 的 metaclass 设置成 MyMeta，MyClass 就不再由原生的 type 创建，而是会调用 MyMeta 的__call__运算符重载。
class = MyMeta(classname, superclasses, attributedict)


# 理解metaclass 装饰器


class Mymeta(type):
  def __init__(self, name, bases, dic):
    super().__init__(name, bases, dic)
    print('===>Mymeta.__init__')
    print(self.__name__)
    print(dic)
    print(self.yaml_tag)

  def __new__(cls, *args, **kwargs):
    print('===>Mymeta.__new__')
    print(cls.__name__)
    return type.__new__(cls, *args, **kwargs)

  def __call__(cls, *args, **kwargs):
    print('===>Mymeta.__call__')
    obj = cls.__new__(cls)
    cls.__init__(cls, *args, **kwargs)
    return obj

class Foo(metaclass=Mymeta):
  yaml_tag = '!Foo'

  def __init__(self, name):
    print('Foo.__init__')
    self.name = name

  def __new__(cls, *args, **kwargs):
    print('Foo.__new__')
    return object.__new__(cls)

foo = Foo('foo')
