# 获取、修改、删除
# 只有获取可以有return

class Foo:
    @property
    def AAA(self):
        print('get的时候运行我啊')

    @AAA.setter
    def AAA(self, value):
        print('set的时候运行我啊')

    @AAA.deleter
    def AAA(self):
        print('delete的时候运行我啊')


f = Foo()
f.AAA
f.AAA = 'set'
del f.AAA
