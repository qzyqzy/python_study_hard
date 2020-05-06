# 对对象的反射

class Foo:
    f = '类的静态变量'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f'hi,{self.name}')


obj = Foo('egon', 73)

# hasattr
print(hasattr(obj, 'age'))  # True
print(hasattr(obj, 'say_hi'))  # True

# getattr
print(getattr(obj, 'age'))  # 73
getattr(obj, 'say_hi')()  # hi,egon

# setattr delattr 不常用
setattr(obj, 'sex', '男')
print(hasattr(obj, 'sex'))  # True
print(obj.sex)  # 男

#
delattr(obj, 'sex')

print(hasattr(obj, 'sex'))  # False
