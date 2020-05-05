print(type('abc'))
print(type(True))
print(type(100))
print(type([1, 2, 3]))
print(type({'name': '太白金星'}))
print(type((1, 2, 3)))
print(type(object))


class A:
    pass


print(isinstance(object, type))  # True
print(isinstance(A, type))  # True

# object是type类的实例，而type类是object类的子类
