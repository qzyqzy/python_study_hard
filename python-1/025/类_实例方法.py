# 定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）；
# 调用：只能由实例对象调用。

class S:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f'{self.name} study')


s = S('qzy')
s.study()  # qzy study
