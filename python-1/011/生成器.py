"""
    生成器的本质就是迭代器，在python社区中，大多数时候都把迭代器和生成器是做同一个概念
    生成器和迭代器也有不同，唯一的不同就是：迭代器都是Python给你提供的已经写好的工具或者通过数据转化得来的，（比如文件句柄，iter([1,2,3])
    生成器是需要我们自己用python代码构建的工具
"""


# python 有三种方式创建生成器
# 1.通过生成器函数、2.通过生成器推导式、3.python内置函数或者模块提示（1、3本质一样）

# 1.生成器函数
def log():
    return 'log'


print(log())  # log


# 将log函数中的return 换为 yield 此时就为一个生成器函数了

def log2():
    yield 'log'


# 返回生成器对象
print(log2())  # <generator object log2 at 0x000001C89FF7E200>

# 生成器的本质就是迭代器 所以取值调用__next__()方法
print(log2().__next__())  # log


# 函数中可以写多个yield,调用时__next__多的话也会报错

def log3():
    yield 4
    yield 5
    yield 6


l = log3()
print(l.__next__())  # 4 next(l)
print(l.__next__())  # 5 next(l)
print(l.__next__())  # 6 next(l)


# yield from
# 可以直接把可迭代对象中的每一个数据作为生成器的结果返回

def yd():
    yield [1, 2, 3, 4]


print(next(yd()))  # [1, 2, 3, 4]


def ydf():
    yield from [1, 2, 3, 4]  # 1


print(next(ydf()))  # 1

# 推导式

# 列表推导式
#   1.循环模式：[变量(加工的变量) for 变量 in iterable]
#   2.筛选模式: [变量(加工的变量) for 变量 in iterable if 条件]

# 循环模式
l1 = [i for i in range(3)]
print(l1)  # [0,1,2]

l1 = [i ** 2 for i in range(3)]
print(l1)  # [0, 1, 4]

# 筛选模式
l1 = [i for i in range(10) if i > 4]
print(l1)  # [5, 6, 7, 8, 9]

# 生成器表达式
"""
   生成器表达式和列表推导式的语法上一模一样,只是把[]换成()就行了。比如将十以内所有数的平方放到一个生成器表达式中 
"""

l4 = (i ** 2 for i in range(10))
print(l4)  # <generator object <genexpr> at 0x0000023123EAE4A0>

"""
    生成器表达式和列表推导式的区别
        1.列表推导式比较耗内存,所有数据一次性加载到内存。而.生成器表达式遵循迭代器协议，逐个产生元素
        2.得到的值不一样,列表推导式得到的是一个列表.生成器表达式获取的是一个生成器
        3.列表推导式一目了然，生成器表达式只是一个内存地址    
"""

# 内置函数
