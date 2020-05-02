# 单继承
class Aniaml(object):
    type_name = '动物类'

    def __init__(self, name, sex, age):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print('吃东西')


# 继承 Animal
class Person(Aniaml):
    def __init__(self, name, sex, age, mind):
        self.mind = mind

        # 执行本身的 __init__方法与父类的__init__方法
        # super(Person,self).__init__(name,sex,age)  # 方法二
        super().__init__(name, sex, age)  # 方法二

    def eat(self):
        super().eat()
        print(f'{self.name}吃饭,{self.mind}')


p = Person('qzy', '女', 18, '远大理想')
p.eat()

# 吃东西
# qzy吃饭,远大理想
