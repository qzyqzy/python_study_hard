# 定义：使用装饰器 @ staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；
#
# 调用：实例对象和类对象都可以调用

# 可以理解为，静态方法是个独立的、单纯的函数，它仅仅托管于某个类的名称空间中，便于使用和维护

import time


class TimeTest(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S", time.localtime())


print(TimeTest.showTime())
