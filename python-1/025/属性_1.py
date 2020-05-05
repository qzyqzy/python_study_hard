class People:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def bmi(self):
        return self.weight / (self.height ** 2)


p1 = People('egon', 75, 1.85)
print(p1.bmi())  # 21.913805697589478


# 属性
# 将一个类的函数定义成特性以后，对象再去使用的时候obj.name,根本无法察觉自己的name是执行了一个函数然后计算出来的，这种特性的使用方式遵循了统一访问的原则

class Peo:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    @property
    def bmi(self):
        return self.weight / (self.height ** 2)


p1 = Peo('egon', 75, 1.85)

# 以属性的方式调用
print(p1.bmi)  # 21.913805697589478
