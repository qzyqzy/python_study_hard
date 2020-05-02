# 依赖关系：将一个类的对象或者类名传到另一个类的方法使用
# 我⽤着你. 但是你不属于我. 这种关系是最弱的

class Elphant:
    def __init__(self, name):
        self.name = name

    def eOpen(self, re):
        print(f'小象{self.name}打开了{re.name}冰箱的门')
        re.rOpen()


class Refrigerator:
    def __init__(self, name):
        self.name = name

    def rOpen(self):
        print(f'{self.name}冰箱的门打开了')


e = Elphant('象象')
re = Refrigerator('冰冰')
e.eOpen(re)
# 小象象象打开了冰冰冰箱的门
# 冰冰冰箱的门打开了
