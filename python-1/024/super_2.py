class A:
    def f1(self):
        print('in A')


class Foo(A):
    def f1(self):
        super().f1()
        print('in Foo')


class Bar(A):
    def f1(self):
        print('in Bar')


class Info(Foo, Bar):
    def f1(self):
        super().f1()
        print('in Info f1')


# [Info, Foo, Bar, A]
print(Info.mro())
obj = Info()
obj.f1()
# in Bar
# in Foo
# in Info f1
