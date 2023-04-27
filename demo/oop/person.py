class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private attribute

    def getage(self):
        return self.__age

    @property   # getter method 
    def category(self):
        if self.__age < 30:
            return "Young"
        else:
            return "Old"



p1 = Person("Jeff", 40)
print(p1.category)  # property

print(p1.__dict__)
print(p1._Person__age)  # Wrong
print(p1.getage())  # Right
