# 整型
# 32位 -2 ** 31 ~~~ 2 ** 31 - 1
# 64位 -2 ** 63 ~~~ 2 ** 63 - 1

"""
python2 中整型有 int long  除法获取到的是整数
python3 中整型有 int       除法获取到的是浮点数
"""

# 十进制与二进制的转化
# 除以对应的进制数、一直除到商1为止 从下往上的余数值

# 56
# 56除2
# 56    0
# 28    0
# 14    0
# 7     1
# 3     1
# 1     1
print(bin(56))  # 0b111000

# 0b111000
print(1 * 2 ** 5 + 1 * 2 ** 4 + 1 * 2 ** 3)  # 56
print(int('111000', 2))  # 56

# bool()
# 非0的数字即为真
# 非空的字符串也为真
print(bool(0))  # False
print(bool(-0))  # False
print(bool(1))  # True
print(bool(''))  # False
print(bool(' '))  # True
