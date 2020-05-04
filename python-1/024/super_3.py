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
        # 执行其他类
        super(Foo, self).f1()
        print('in Info f1')


# [Info, Foo, Bar, A]
print(Info.mro())

obj = Info()
obj.f1()
# in Bar
# in Info f1

# super(S, self) 严格按照self的从属类的mro顺序、执行S类的下一个
# 执行 Foo类的下一个 从Bar类开始执行
