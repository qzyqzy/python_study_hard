lst = ['qzy', 123, True]
print(lst[0])  # qzy
print(id(lst[0]))
# id 获取对象的内存地址
lst[0] = 'qzyqzy'
print(lst[0])  # qzyqzy
print(id(lst[0]))

'''
增
'''

lst.append('is')
print(lst)  # ['qzyqzy', 123, True, 'is']

lst.insert(2, 'are')
print(lst)  # ['qzyqzy', 123, 'are', True, 'is']

# 可以for循环的即可
lst.extend('123')
print(lst)  # ['qzyqzy', 123, 'are', True, 'is', '1', '2', '3']

'''
删
'''

# 默认删除最后一个
lst.pop()
print(lst)  # ['qzyqzy', 123, 'are', True, 'is', '1', '2']

lst.pop(0)
print(lst)  # [123, 'are', True, 'is', '1', '2']

# 如果存在多个同名的 也只会删除第一个
lst.remove('1')
print(lst)  # [123, 'are', True, 'is', '2']

# del lst
# print(lst)
# name 'lst' is not defined


del lst[:-2]
print(lst)  # ['is', '2']

lst.clear()
print(lst)  # []

'''
改
'''

lst = ['1', '2', '3', '4']

lst[0] = '5'
print(lst)  # ['5', '2', '3', '4']

lst[0:2] = '9876543210'  # 此时的值必须可循环
print(lst)  # ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0', '3', '4']

lst = ['1', '2']
lst[:1] = 9, 8, 7, 6, 5
print(lst)  # [9, 8, 7, 6, 5, '2']

# 步长不为1时要一一对应 不能多也不能少
lst = [1, 2, 3, 4, 5]
lst[:3:2] = '91'
print(lst)  # ['9', 2, '1', 4, 5]
