name = 'qzy'

# [ 起始位置 : 终止位置 ： 步长 ] 步长不仅能决定位置也能决定方向 默认为1
# 取到z的值
# 从左往右 0 1 2
print(name[1])  # z

# 从右往左 -3 -2 -1
print(name[-2])  # z

# 取到qz的值
# [] 顾头不顾尾 可以不填 默认为0或者最后位置
print(name[0:2])  # qz
print(name[0:-1])  # qz

# 取到zy的值
print(name[1:3])  # zy
print(name[1:])  # zy

# 取yz的值
print(name[:-3:-1])  # yz

print(name[-2:2])  # z  不会相互抵消

# 步长
name = 'my name is qzy'
print(name[:])  # my name is qzy
print(name[::2])  # m aei z

# print(name[100])  此时会报错
print(name[100:105])  # 空 但不会报错
print(name[-100:])  # my name is qzy
print(name[-3:])    # qzy

