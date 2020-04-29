# 算术运算符
print(3 + 4)  # 7
print(3 - 4)  # -1
print(3 * 4)  # 12
print(3 / 4)  # 0.75 python2 获取到的是整数  python 获取到的是浮点数
print(1 / 3)  # 0.3333333333333333
print(10 // 3)  # 整除（地板除） 3
print(10 % 3)  # 1
print(3 ** 3)  # 幂（次方） 27

# 比较运算符
print(3 > 4)  # False
print(3 >= 4)  # False
print(3 < 4)  # True
print(3 <= 4)  # True
print(3 == 4)  # False
print(3 != 4)  # True

# 赋值运算符
# =  += -= ...

# 逻辑运算符
# not and or 没有符号
# 优先级 not > and > or
print(not True)  # False
print(1 and 2)  # 2
print(1 or 2)  # 1

# 成员运算符
nameStr = 'qzyname'
print('qzy' in nameStr)  # True
print('qzy1' not in nameStr)  # True
