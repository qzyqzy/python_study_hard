# 序列化模块
#   列化的本质就是将一种数据结构（如字典、列表)等转换成一个特殊的序列（字符串或者bytes）的过程就叫做序列化
#   一个特殊的序列，而不是我们常用的str这种字符串

# 为什么要有序列化模块
#   序列化模块就是将一个常见的数据结构转化成一个特殊的序列，并且这个特殊的序列还可以反解回去。它的主要用途：文件读写数据，网络传输数据

# json模块
#   json 序列化只支部分python数据结构 dict\list\tuple\str\int\float\bool\None

# pickle模块
#   只能在python中使用、支持python中的所有数据

# json 模块
#   用于网络传输 dumps、loads
#   用于文件读写 dump、load

import json

dic = {'name': 'qzy', 'age': 19}
strDic = json.dumps(dic)
print(type(strDic), strDic)  # <class 'str'> {"name": "qzy", "age": 19}

dic2 = json.loads(strDic)
print(type(dic2), dic2)  # <class 'dict'> {'name': 'qzy', 'age': 19}

f = open('json.json', 'r+')
# dump、load接收一个文件句柄，可以直接处理文件
# json.dump(dic, f)

# dic3 = json.load(f)
# print(dic3)  # {'name': 'qzy', 'age': 19}
