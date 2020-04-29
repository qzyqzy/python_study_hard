
# demo1

# 存储的是内存地址
s = '人生啊'
a = [1, 2, 3, s]
s = '人生'
print(a)  # [1, 2, 3, '人生啊']

# demo2

a = [1, 2, 3]
b = {'age': a}
a.append(4)
print(b)  # {'age': [1, 2, 3, 4]}
a = 123
print(b)  # {'age': [1, 2, 3, 4]}
