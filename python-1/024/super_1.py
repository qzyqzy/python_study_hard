# super()严格按照类的mro顺序执行
# super(S, self) 严格按照self的从属类的mro顺序、执行S类的下一个

class A:
    def f1(self):
        print('in A f1')

    def f2(self):
        print('in A f2')


class Foo(A):
    def f1(self):
        super().f2()
        print('in A Foo')


# [Foo, A]
print(Foo.mro())
obj = Foo()
obj.f1()
# in A f2
# in A Foo
