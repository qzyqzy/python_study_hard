name = 'my name is Qzy'
#  upper() 大写
print(name.upper())  # MY NAME IS QZY

# lower() 小写
print(name.lower())  # my name is qzy

# 是否以什么开头
# startswith('my', start, end)
print(name.startswith('my'))  # True
print(name.startswith('my', 2))  # False 从下标为2的位置开始

# 是否以什么结尾
# endswith('zy', start, end)
print(name.endswith('zy'))  # True
print(name.endswith('zy', 0, 3))  # False

# 统计次数
# count()
print(name.count('m'))  # 2

# 去除前后两端相应的字符串
# 该方法只能删除开头或是结尾的字符，不能删除中间部分的字符
name = '  my name is name  '
# 去除前后的空格 \n \t
print(name.strip())  # my name is name
name = 'my name is name'
# 去除字符中的y
print(name.strip('m'))  # y name is name

'''
多个字符的 会去除前后的b与be两个 分别去筛选
'''
name = 'eqzybabe'
print(name.strip('be'))  # qzyba

# 分割
print(name.split())  # ['eqzybabe']
print(name.split('e'))  # ['', 'qzybab', '']

name = 'qzyzyq'
print(name.split('z'))  # ['q', 'y', 'yq']
print(name.split('z', maxsplit=1))  # ['q', 'yzyq']

print(name.rsplit('z', maxsplit=1))  # ['qzy', 'yq']

# 替换
name = 'qzy is sex'
print(name.replace('s', 'l'))  # qzy il lex
print(name.replace('s', 'l', 1))  # qzy il sex
