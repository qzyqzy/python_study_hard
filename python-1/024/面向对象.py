# 封装、继承、多态


# 鸭子类型
# 你看起来像鸭子，那么你就是鸭子

class A:
    def f1(self):
        print('in A f1')

    def f2(self):
        print('in A f2')


class B:
    def f1(self):
        print('in A f1')

    def f2(self):
        print('in A f2')

# A 和 B两个类完全没有耦合性，但是在某种意义上他们却统一了一个标准。
# 对相同的功能设定了相同的名字，这样方便开发，这两个方法就可以互成为鸭子类型。

# 这样的例子比比皆是：str  tuple list 都有 index方法，这就是统一了规范。
# str bytes 等等 这就是互称为鸭子类型。
