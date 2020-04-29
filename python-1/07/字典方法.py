# popitem
# 返回并删除字典中的最后一对键和值
# 字典已经为空，却调用了此方法，就报出 KeyError 异常

dic = {'name': 'qzy', 2: '2', 1: '1'}
dic.popitem()
print(dic)  # {'name': 'qzy', 2: '2'}

# fromkeys
# 创建一个新字典
# 以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值 
# 值会被公用
dic = dict.fromkeys((1, 2, 3))
print(dic)  # {1: None, 2: None, 3: None}

dic = dict.fromkeys((1, 2), 4)
print(dic)  # {1: 4, 2: 4}
