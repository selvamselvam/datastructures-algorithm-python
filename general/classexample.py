class Dog:
    name = 'Selvam'

    def __init__(self, namevl):
        self.localname = namevl


x = Dog('one')
y = Dog('two')

print(x.name)
print(y.name)
print(x.localname)
print(y.localname)
