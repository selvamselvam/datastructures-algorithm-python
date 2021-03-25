str = 'Hello'
import copy

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


student = Student('siva', 12)
student.myfunc()

list=[1,2,3,4,5,6]
list2 = copy.deepcopy(list)
print("list and list2 after deep copy")
print(list)
print(list2)

print("list and list2 after change list element")
list[4]=9
print(list)
print(list2)
