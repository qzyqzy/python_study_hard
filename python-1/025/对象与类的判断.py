# isinstance(a,b)：判断a是否是b类（或者b类的派生类）实例化的对象
# issubclass(a,b)： 判断a类是否是b类（或者b的派生类）的派生类

class A:
    pass


class B(A):
    pass


class C(B):
    pass


obj = B()

print(isinstance(obj, B))  # True
print(isinstance(obj, A))  # True

print(issubclass(B, A))  # True
print(issubclass(C, A))  # True
