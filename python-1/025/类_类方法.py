# 定义：使用装饰器 @ classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）；
#
# 调用：实例对象和类对象都可以调用。


# 类方法可以实例化对象
# 可以操作类中的属性

class S:
    count = 0

    def __init__(self, name):
        self.name = name
        S.add_count()

    def study(self):
        print(f'{self.name} study')

    @classmethod
    def add_count(cls):
        S.count += 1

    @classmethod
    def get_count(cls):
        return S.count


s = S('qzy')
s = S('qzy')
s = S('qzy')
print(S.count)
