"""
 字典 （对象） dict
"""

# 字典的键 必须是不可哈希的 即不可变的数据类型
name = {
    'age': 16,
    (1, 2): 1,
    True: 123
}
print(name)

'''
错误
'''
# name = {[1, 2]: '17'}  # unhashable type: 'list'

"""
增
"""

dic = {}

dic['1'] = 1
print(dic)  # {'1': 1}

dic.setdefault('2', 2)
print(dic)  # {'1': 1, '2': 2}

# 如果键名已存在，不做修改
dic.setdefault('1', 3)
print(dic)  # {'1': 1, '2': 2}

"""
删
"""

del dic['1']
print(dic)  # {'2': 2}

dic.pop('2')
print(dic)  # {}

dic.clear()
print(dic)  # {}

"""
改
"""

# 有则改 无则新增

dic = {'1': 1, '2': 2, '3': 3}

dic['1'] = '4'
print(dic)  # {'1': '4', '2': 2, '3': 3}

dic.update({'3': 5})
print(dic)  # {'1': '4', '2': 2, '3': 5}

"""
查
"""

dic = {'1': 'qzy', '2': 'qxy'}

for i in dic:
    # 键名
    print(i)  # 1 2

print(dic.get('1'))  # qzy
print(dic.get('3'))  # None

print(dic['1'])  # qzy
# print(dic['3123'])  # 会报错 推荐使用get
