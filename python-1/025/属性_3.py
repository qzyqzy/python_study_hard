class Foo:
    def get_AAA(self):
        print('get的时候运行我啊')

    def set_AAA(self, value):
        print('set的时候运行我啊')

    def delete_AAA(self):
        print('delete的时候运行我啊')

    AAA = property(get_AAA, set_AAA, delete_AAA)  # 内置property三个参数与get,set,delete一一对应


f1 = Foo()
f1.AAA
f1.AAA = 'aaa'
del f1.AAA
