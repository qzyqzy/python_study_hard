"""
实参的角度（数量一一对应）
    1. 位置参数
    2. 关键字参数
    3. 混合参数
形参的角度
    1. 位置参数
    2. 默认参数
    3. 动态参数
    4. 仅限关键字参数
"""


# 实参角度

# 位置参数 一一对应
def add(a, b):
    return a + b


print(add(4, 5))  # 9


# 关键字参数 顺序不用一一对应、数量也要对应上

def say(name, age):
    return f'我的名字是{name},年龄是{age}'


# print(say(age=18)) missing 1 required positional argument: 'name'
# print(say(age=18, name='qzy', sex='女')) say() got an unexpected keyword argument 'sex'
print(say(age=18, name='qzy'))  # 我的名字是qzy,年龄是18


# 混合参数
# 关键字参数一定要放在位置参数后面 、数量一一对应 、已经传值的不允许再次传值

def say2(name, age, sex):
    return f'我的名字是{name},年龄是{age},性别是{sex}'


print(say2('qzy', sex='男', age=18))  # 我的名字是qzy,年龄是18,性别是男


# 形参角度
# 位置参数与实参保持一致

# 默认参数
# 默认参数一定要放在位置参数后面
def say3(name, age, sex='男'):
    return f'我的名字是{name},年龄是{age},性别是{sex}'


print(say3('qzy', age=18))  # 我的名字是qzy,年龄是18,性别是男
print(say3('qzy', 18, '女'))  # 我的名字是qzy,年龄是18,性别是女
print(say3('qzy', age=18, sex='女女'))  # 我的名字是qzy,年龄是18,性别是女女


# 动态参数 万能参数 将实参的所有参数聚合到一个元组中
def sun(*args):
    return args


print(sun(1, 2, 3))  # (1, 2, 3)


# **kwargs 将所有关键字参数聚合成一个字典
def sun1(**kwargs):
    return kwargs


print(sun1(name=18, age=18))  # {'name': 18, 'age': 18}

# *的更多用法
# *iterable 可遍历对象
print(*[1, 2, 3])  # 1 2 3


def say4(age, name):
    return f'我的名字是{name},年龄是{age}'


print(say4(**{'name': 'qzy', 'age': 18}))  # 我的名字是qzy,年龄是18

a, b, *c = [1, 2, 3, 4]
print(c)  # [3, 4]

a, b, *c = (1, 2, 3, 4)
print(c)  # [3, 4]


# 参数位置顺序
# 正确顺序
def sum4(a, b, c, *args, d='7', **kwargs):
    print(a, b, c, args, d, kwargs)

# 仅限关键字参数
# 放到 *args与**kwargs之间只能以关键字参数传递
