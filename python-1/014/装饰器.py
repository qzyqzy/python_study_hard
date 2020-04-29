"""
开放封闭原则
    1：对扩展是开放的
        我们说，任何一个程序，不可能在设计之初就已经想好了所有的功能并且未来不做任何更新和修改。所以我们必须允许代码扩展、添加新功能
    2：对修改是封闭的
       因为我们写的一个功能，很有可能已经交付给其他人使用了，如果这个时候我们对函数内部进行修改，或者修改了函数的调用方式，很有可能影响其他已经在使用该函数的用户
    装饰器最终最完美的定义就是：在不改变原被装饰的函数的源代码以及调用方式下，为其添加额外的功能
"""

import time


# 定义一个函数返回相加的和
def add(x, y):
    time.sleep(2)
    return x + y


print(add(4, 5))  # 9


# 现在我们编写一个测试函数执行时间的函数
def timmer(f):
    start_time = time.time()
    print(f(5, 5))  # 10
    end_time = time.time()
    print(f'此函数的执行效率为{end_time - start_time}')  # 此函数的执行效率为2.001023530960083


timmer(add)

"""
    开放封闭原则
        add函数除了完成了自己之前的功能，还增加了一个测试执行效率的功能，对不？所以也符合开放原则
        index函数源码改变了么？没有，但是执行方式改变了，所以不符合封闭原则
        因为要想调用测试时间的代码 不是直接调用的add(5,5)  
"""


# 实现真正的开放封闭原则：装饰器
# 带返回值的装饰器
# 被装饰函数带参数的装饰器
def timer2(f):
    def inner(x, y):
        start_time = time.time()
        ret = f(x, y)
        end_time = time.time()
        print(f'此函数的执行效率为{end_time - start_time}')
        return ret

    return inner


add = timer2(add)
print(add(6, 6))  # 12


# 5. 标准版装饰器
# 代码优化：语法糖
#  如果你想给add加上装饰器，每次执行add之前你要写上一句：add = timer2(add)这样你在执行add函数 才是真生的添加了额外的功能。但是每次写这一句也是很麻烦。所以，Python给我们提供了一个简化机制，用一个很简单的符号去代替这一句话
def timer3(f):
    def inner(x, y):
        start_time = time.time()
        ret = f(x, y)
        end_time = time.time()
        print(f'此函数的执行效率为{end_time - start_time}')
        return ret

    return inner


@timer3  # 等同于 add3 = timer3(add3)
def add3(x, y):
    time.sleep(2)
    return x + y


print(add3(7, 7))  # 14
