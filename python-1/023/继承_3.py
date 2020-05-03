# 多继承
class ShenXian:  # 神仙
    def fei(self):
        print("神仙都会⻜")


class ShenXian:
    def fei(self):
        print("神仙可以飞")


class Monkey:
    def chitao(self):
        print("猴⼦喜欢吃桃⼦")


class SunWukong(ShenXian, Monkey):  # 孙悟空是神仙, 同时也是⼀只猴
    pass


sxz = SunWukong()
sxz.chitao()  # 猴⼦喜欢吃桃⼦
sxz.fei()  # 神仙可以飞
