# f = open('文件地址',mode="文件打开模式",encoding="编码格式")
# f 文件句柄
# 文件操作步骤 1：打开文件  2：读写文件  3：关闭文件
f = open('read.txt', mode='r', encoding='utf-8')
# 文件读完会接着上次的内容 所以再次调用不会返回数据

# read() 全部读取
# read(3) 3个字符
print(f.read())
print(f.read())
# 1
# 2
f.close()

# readline() 读取一行文件内容
f = open('read.txt', mode='r', encoding='utf-8')
print(f.readline())  # 1 实际获取的内容为'1\n'
print(f.readline().strip())  # 2 实际获取的内容为'2\n'
f.close()

# readlines 一行一行的读取 放在列表中
f = open('read.txt', mode='r', encoding='utf-8')
print(f.readlines())  # ['1\n', '2']
f.close()

f = open('read.txt', mode='r', encoding='utf-8')

# 大文件读取
for i in f:
    print(i)

f.close()

"""
文件写操作
"""

# w 先清空文件再写入
f = open('write.txt', mode='w', encoding='utf-8')
print(f.write('123456'))  # 返回写入的字符数
print(f.write('123456'))
f.close()

# a 追加
f = open('write.txt', mode='a', encoding='utf-8')
f.write('654321')
f.close()

# 路径转义
# \ 全部写成 \\
# 'C:\\Users\\dullwinnie\\Desktop\\python-demo'
# r"C:\\Users\\dullwinnie\\Desktop\\python-demo"
