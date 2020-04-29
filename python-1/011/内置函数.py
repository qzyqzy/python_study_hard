# 返回函数的绝对值
print(abs(-5))  # 5

# 求和
print(sum([1, 2, 3]))  # 6
print(sum((1, 2, 3), 4))  # 10

# 最小值

# 此序列的最小值
print(min([1, 2, 3]))  # 1

# 按绝对值的大小,返回此序列的最小值
print(min([1, 2, -5], key=abs))  # 1

# 加key是可以加函数名，min自动会获取传入函数中的参数的每个元素，然后通过你设定的返回值比较大小，返回最小的传入的那个参数

print(min([1, 2, -5], key=lambda x: x ** 3))  # -5
print(min([1, 2, -5], key=lambda x: x ** 2))  # 1

# max() 最大值与最小值用法相同

# 序列翻转
# 获取到的是一个生成器
print(list(reversed([1, 2])))  # [2, 1]

# bytes() 把字符串转换为bytes类型
s = '您好'
print(bytes(s, encoding='utf-8'))  # b'\xe6\x82\xa8\xe5\xa5\xbd'

# zip() 拉链方法
# 函数用于将可迭代的对象作为参数,将对象中对应的元素打包成一个个元组
# 然后返回由这些元祖组成的内容,如果各个迭代器的元素个数不一致,则按照长度最短的返回

ls1 = [0, 1]
ls2 = [2, 3, 4, 5]
ls3 = [5, 6, 7]
for i in zip(ls1, ls2, ls3):
    print(i)
# (0, 2, 5)
# (1, 3, 6)
