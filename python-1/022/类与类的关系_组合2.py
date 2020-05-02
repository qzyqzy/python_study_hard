class Gamerole:
    def __init__(self, name, ad, hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    def attack(self, p1):
        p1.hp -= self.ad
        print(f'{self.name}攻击{p1.name},{p1.name}掉了{self.ad}血,还剩{p1.hp}血')

    # 组合：给一个对象封装一个属性改属性是另一个类的对象
    # 调用此方法将武器类封装到英雄属性中
    def equip_weapon(self, wea):
        self.wea = wea


class Weapon:
    def __init__(self, name, ad):
        self.name = name
        self.ad = ad

    def weapon_attack(self, p1, p2):
        p2.hp = p2.hp - self.ad - p1.ad
        print(f'{p1.name} 利用 {self.name} 攻击了{p2.name},{p2.name}还剩{p2.hp}血')


gaiLun = Gamerole('盖伦', 10, 200)
yaSuo = Gamerole('亚索', 50, 80)

pillow = Weapon('绣花枕头', 2)

# 给人物装备武器对象
gaiLun.equip_weapon(pillow)

# 英雄开始攻击
gaiLun.wea.weapon_attack(gaiLun, yaSuo)  # 盖伦 利用 绣花枕头 攻击了亚索,亚索还剩68血
gaiLun.wea.weapon_attack(gaiLun, yaSuo)  # 盖伦 利用 绣花枕头 攻击了亚索,亚索还剩56血
gaiLun.wea.weapon_attack(gaiLun, yaSuo)  # 盖伦 利用 绣花枕头 攻击了亚索,亚索还剩44血
