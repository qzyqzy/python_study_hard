# 组合：将一个类的对象封装到另一个类的对象的属性中，就叫组合

# 实现英雄互殴

class Gamerole:
    def __init__(self, name, ad, hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    def attack(self, p1):
        p1.hp -= self.ad
        print(f'{self.name}攻击{p1.name},{p1.name}掉了{self.ad}血,还剩{p1.hp}血')


class Weapon:
    def __init__(self, name, ad):
        self.name = name
        self.ad = ad

    def weapon_attack(self, p1, p2):
        p2.hp = p2.hp - self.ad - p1.ad
        print(f'{p1.name} 利用 {self.name} 攻击了{p2.name},{p2.name}还剩{p2.hp}血')


gaiLun = Gamerole('盖伦', 10, 200)
yaSuo = Gamerole('亚索', 50, 80)

# 此处发起者是武器 应该是英雄发起
pillow = Weapon('绣花枕头', 2)
pillow.weapon_attack(gaiLun, yaSuo)  # 盖伦 利用 绣花枕头 攻击了亚索,亚索还剩68血

# 但是上面这么做不好，利用武器攻击也是人类是动作的发起者，所以不能是pillow武器对象，而是人类利用武器攻击对方
# 所以利用组合将武器类封装到英雄属性中
