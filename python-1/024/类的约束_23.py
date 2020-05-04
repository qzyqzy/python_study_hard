# 使⽤元类来描述⽗类. 在元类中给出⼀个抽象⽅法. 这样⼦类就不得不给出抽象⽅法的具体实现. 也可以起到约束的效果.

from abc import ABCMeta, abstractmethod


# 如果子类未定义pay方法就会报错
class Payment(metaclass=ABCMeta):  # 抽象类 接口类  规范和约束  metaclass指定的是一个元类
    @abstractmethod
    def pay(self, money): pass  # 抽象方法


class QQpay(Payment):
    def pay(self, money):
        print('使用qq支付%s元' % money)


class Alipay(Payment):
    def pay(self, money):
        print('使用阿里支付%s元' % money)


class WeChatpay(Payment):
    pass


def pay(obj, money):  # 这个函数就是统一支付规则，这个叫做： 归一化设计。
    obj.pay(money)


a = Alipay()
b = QQpay()
w = WeChatpay()

pay(a, 100)
pay(b, 200)
# 使用阿里支付100元
# 使用qq支付200元
