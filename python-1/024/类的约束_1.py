# 推荐此写法
# 如果不按套路出牌 不执行已定义的方法，此pay方法不一定执行
# 约定俗成的
# 提取⽗类. 然后在⽗类中定义好⽅法. 在这个⽅法中什么都不⽤⼲. 就抛⼀个异常就可以了. 这样所有的⼦类都必须重写这个⽅法. 否则. 访问的时候就会报错.

class Payment:
    """
        此类什么都不做，就是制定一个标准，谁继承我，必须定义我里面的方法。
    """

    def pay(self, money):
        #    pass
        #    or
        # 执行父类的方法时 报错 子类未重写pay方法
        raise Exception("此pay方法必须重写")


class QQpay(Payment):
    def pay(self, money):
        print('使用qq支付%s元' % money)


class Alipay(Payment):
    def pay(self, money):
        print('使用阿里支付%s元' % money)


class WeChatpay(Payment):
    def pay1(self, money):
        print('使用微信支付%s元' % money)


def pay(obj, money):  # 这个函数就是统一支付规则，这个叫做： 归一化设计。
    obj.pay(money)


a = Alipay()
b = QQpay()
w = WeChatpay()

pay(a, 100)
pay(b, 200)
# 使用阿里支付100元
# 使用qq支付200元
pay(w, 20)
