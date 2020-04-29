dic = {'name': 'qzy', 'age': 16}

# 获取所有的key值
# 得到的值 是类 list 支持for循环 不支持 索引
print(dic.keys())  # dict_keys(['name', 'age'])
for i in dic.keys():
    print(i)
'''
name
age
'''

# 想得到真正的数组 需要转换一下
print(list(dic.keys()))  # ['name', 'age']

# 获取所有的值
print(list(dic.values()))  # ['qzy', 16]

# 获取键和值
print(list(dic.items()))  # [('name', 'qzy'), ('age', 16)]

'''
解构
'''

a = 10, 12  # 10,12 本质就是一个元组 (10,12)
print(a)  # (10,12)

a, b = 10, 12
print(a, b)  # 10 12

a, b = '45'
print(a, b)  # 4 5

a, b = {'q': 'qzy', 'z': 'zy'}
print(a, b)  # q z  循环的也是键值
