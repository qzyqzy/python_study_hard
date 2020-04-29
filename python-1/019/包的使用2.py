# 第二类
# 第二类：执行文件通过 from ... import 导入包以及包内的功能

# 不用修改__init__.py文件

from tool2 import add

print(add.add(1, 2))  # 3

from tool2.inner import inner

print(inner.inner(3, 5))  # 15

# 引用的规则
# from a.b.c.d import e
# .d的前面一定是包名 import的后面一定没有.
