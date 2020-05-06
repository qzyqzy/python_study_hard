class Foo:
    f = '类的静态变量'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f'hi,{self.name}')


print(hasattr(Foo, 'say_hi'))  # True

# self 以类的方式调用 self没有自动传入
getattr(Foo, 'say_hi')(Foo('qzy', 18))  # hi,qzy
