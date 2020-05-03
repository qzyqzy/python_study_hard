# 多继承的查找顺序
# 遵循mro算法
class A:
    pass


class B(A):
    pass


class C(A):
    def say(self):
        print('C')

    pass


class D(B, C):
    def say(self):
        print('D')

    pass


class E:
    pass


class F(D, E):
    pass


class G(F, D):
    pass


class H:
    pass


class Foo(H, G):
    pass


print(Foo.mro())
# [<class '__main__.Foo'>, <class '__main__.H'>, <class '__main__.G'>, <class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.E'>, <class 'object'>]

# [Foo, H, G, F, D, B, C, A, E]

f = Foo()

# 按照上面的顺序查找方法
f.say()
