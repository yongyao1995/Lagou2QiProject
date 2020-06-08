def f():
    return 'hello word'


class MyClass(object):
    i = 123


use_class = MyClass()
print(f"调用类的属性： {use_class.i}")
print(f"调用类的方法：{f()} ")
