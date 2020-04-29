'''
 range() 函数可创建一个整数列表，一般用在 for 循环中。
 range(start, stop[, step])
 start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）
 stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
 step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''
name = range(0, 10)
print(name)
# python3中 写的什么打印什么
# python2中 打印 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(name))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(5)))  # [0, 1, 2, 3, 4]

print(list(range(1, 5)))  # [1, 2, 3, 4]

print(list(range(1, 5, 3)))  # [1, 4]

print(list(range(5, 0, -1)))  # [5, 4, 3, 2, 1]

print(list(range(0, -5, -1)))  # [0, -1, -2, -3, -4]

print(list(range(0)))  # []

print(list(range(5, 0)))  # []

