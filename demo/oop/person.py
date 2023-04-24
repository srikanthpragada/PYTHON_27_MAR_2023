class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age   # private attribute


p1 = Person("Jeff", 40)
#p1.age = 140
print(p1.__age)
