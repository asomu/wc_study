class Person:
    def __init__(self, name='kim', age=30, address='seoul'):
        self.name = name
        self.age = age
        self.address = address
    def print_info(self):
        print('name:{} age:{} address:{}'.format(self.age, self.age, self.address))

obj1 = Person()
obj1.print_info()
obj2 = Person('jang', '40', 'buchen')
obj2.print_info()