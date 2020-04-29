# 字符串是不可变数据
# 方法都是返回新值

# captialize() 把字符串的第一个字符大写 不算空格
print('name'.capitalize())  # Name

# center(width[,fillchar])  返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格
print('name'.center(3, '*'))  # name
print('name'.center(5, '*'))  # *name
print('name'.center(6, '*'))  # *name*

# count  str.count(sub, start= 0,end=len(string)) 用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置
# end 结束位置不包含

print('namename'.count('e'))  # 2
print('namename'.count('e', 3))  # 2
print('namename'.count('e', 3, 7))  # 1
print('namename'.count('qqq'))  # 0

# find 检测字符串中是否包含子字符串 包含返回索引值 否返回-1
# find(str, beg=0, end=len(string))
print('name'.find('me'))  # 2
print('name'.find('qq'))  # -1

# index 与find类似 但是如果查找的字符串不存在会报错

# swapcase 翻转字符串中的大小写
print('nameNAME'.swapcase())  # NAMEname

# title 返回标题化的字符串 单词都已大写开始
print('name is qzy'.title())  # Name Is Qzy
print(('name,is,qzy').title())  # Name,Is,Qzy
print(('nameisqzy').title())  # Nameisqzy

# join 以指定字符串连接生成一个新的字符串
print('_'.join('name'))  # n_a_m_e

# 格式化 通过 {} 和 : 来代替以前的 %

# 不设置指定位置，按默认顺序 参数可以多不可以少
print('name is {} {}'.format('qzy', 'qqq'))  # name is qzy qqq

# 设置指定位置
print('name is {0} {1}'.format('qzy', 'qqq'))  # name is qzy qqq
print('name is {1} {0}'.format('qzy', 'qqq'))  # name is qqq qzy

# 设置参数
print('name is {a} {b}'.format(b='qqq', a='qzy'))  # name is qzy qqq
