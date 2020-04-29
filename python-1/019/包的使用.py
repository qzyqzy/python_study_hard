# 第一类：执行文件通过 import 导入包以及包内的功能
# 第二类：执行文件通过 from ... import 导入包以及包内的功能


# 第一类包的使用


# 创建一个模块 会发生三件事情
"""
    1.将引入的文件加载到内存中
    2.创建一个以该模块命名的名词空间
    3.通过该模块名.的方式引用其模块内的所有内容
"""

# 创建一个包，也会发生三件事
'''
    1.将该包内的__init__.py文件加载到内存中
    2.创建一个以该包名命名的名称空间
    3.通过该包名.模块名.的方式引用__init__的所有内容
'''

import tool

print(tool.add.add1(4, 5))  # 9



