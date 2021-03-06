"""
    存放名字与值的关系’的空间起了一个名字-------命名空间。
    代码在运行伊始，创建的存储“变量名与值的关系”的空间叫做全局命名空间
    在函数的运行中开辟的临时的空间叫做局部命名空间也叫做临时名称空间
    python还有一个空间叫做内置名称空间：内置名称空间存放的就是一些内置函数等拿来即用的特殊的变量：input，print，list等等
"""

"""
    总结
    全局命名空间--> 我们直接在py文件中, 函数外声明的变量都属于全局命名空间
    局部命名空间--> 在函数中声明的变量会放在局部命名空间
    内置命名空间--> 存放python解释器为我们提供的名字, list, tuple, str, int这些都是内置命名空间
"""

# 加载顺序
"""
    所以这三个空间的加载顺序为：内置命名空间(程序运行伊始加载)->全局命名空间(程序运行中：从上到下加载)->局部命名空间(程序运行中：调用时才加载
"""

# 取值顺序

"""
    取值顺序与加载顺序是相反的，取值顺序满足的就近原则，从小范围到大范围一层一层的逐步引用
"""

# 作用域
"""
     全局作用域: 全局命名空间 + 内置命名空间
     局部作⽤域: 局部命名空间
"""

# 内置函数globals(),locals()
# globals(): 以字典的形式返回全局作用域所有的变量对应关系。
# locals(): 以字典的形式返回当前作用域的变量的对应关系。

