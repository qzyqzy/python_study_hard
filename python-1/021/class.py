class Human:
    mind = '思想'

    def work(self):
        print('努力工作')


# 通过__dict__可以查看并获取到所有属性与方法
# 但不通过此方法调用

print(Human.__dict__['mind'])  # 思想
print(Human.__dict__['work'](12))  # 努力工作 None

# 属性通过此方法获取
print(Human.mind)  # 思想
Human.mind2 = '思想2'
print(Human.__dict__)
del Human.mind2
print(Human.__dict__)
