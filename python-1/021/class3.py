class Human:
    mind = '思想'

    def __init__(self, name):
        # 属性一般放到此处
        self.name = name

    def work(self, level):
        self.level = level
        print(f'{level}工作')


h = Human('qzy')
print(h.__dict__)  # {'name': 'qzy'}
h.work('不努力')
print(h.__dict__)  # {'name': 'qzy', 'level': '不努力'}

# 对象只能查看类中的属性
print(h.mind)  # 思想
# 此时修改的是对象空间内的属性 不是类中的属性
h.mind = '123'
print(h.mind)  # 123
print(Human.mind)  # 思想
