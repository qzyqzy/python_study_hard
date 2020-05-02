# class Person:
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#
# class Cat:
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#
# class Dog:
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.age = age
#         self.sex = sex


# 使用继承
class Aniaml(object):
    def __init__(self, name, sex, age):
        self.name = name
        self.age = age
        self.sex = sex


class Person(Aniaml):
    pass


class Cat(Aniaml):
    pass


class Dog(Aniaml):
    pass
