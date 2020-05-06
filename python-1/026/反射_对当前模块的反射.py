import sys


def s1():
    print('s2')


def s2():
    print('s2')


this_module = sys.modules[__name__]

print(hasattr(this_module, 's1'))  # true
getattr(this_module, 's2')()  # s2
