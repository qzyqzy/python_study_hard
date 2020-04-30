class Human:
    mind = '思想'

    def __init__(self):
        self.name = 'qzy'

    def work(self):
        print('努力工作')


h1 = Human()
print(h1.__dict__)  # {'name': 'qzy'}
h1.age = 18
print(h1.__dict__)  # {'name': 'qzy', 'age': 18}
del h1.age
print(h1.__dict__)  # {'name': 'qzy'}
h1.name = 'qzy1'
print(h1.__dict__)  # {'name': 'qzy1'}
