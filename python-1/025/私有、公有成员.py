# 公有成员 类可以访问；类内部可以访问；派生类中可以访问
# 私有成员 仅类内部可以访问

# 私有成员可以通过特殊方法访问

class A:
    name = '公有name'
    __name = '私有name'

    def add(self):
        print('公有add')

    def __add__(self, other):
        print('私有add')


a = A()
print(a.name)  # 公有name
# print(a.__name) 无法访问

# 私有成员实际上是python将_类名加到了属性或者方法前面
# 可以通过这样调用 但不要这样做

print(a._A__name)  # 私有name
