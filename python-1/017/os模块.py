# os模块是与操作系统交互的一个接口

# 当前执行这个python文件的工作目录相关的工作路径
import os

# 获取当前的工作目录
print(os.getcwd())  # C:\Users\dullwinnie\Desktop\python-demo\017

# 返回当前目录
print(os.curdir)  # .

# 获取当前目录的父目录字符串名
print(os.pardir)  # ..

"""
文件夹相关
    os.makedirs('dirname1/dirname2')    可生成多层递归目录  
    os.removedirs('dirname1') 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推 
    os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname 
    os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname 
"""

"""
文件相关
    os.remove()  删除一个文件
    os.rename("oldname","newname")  重命名文件/目录
    os.stat('path/filename')  获取文件/目录信息
"""

"""
path系列
   os.path.abspath(path) 返回path规范化的绝对路径 
   os.path.split(path) 将path分割成目录和文件名二元组返回
   os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
   os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
   os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
   os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
   os.path.getsize(path) 
"""
