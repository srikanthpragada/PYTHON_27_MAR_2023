class Student:
    def __init__(self, admno, name, course='python', feepaid=0):
        self.admno = admno
        self.name = name
        self.course = course
        self.feepaid = feepaid

    def payment(self, amount):
        self.feepaid += amount

    def getfee(self):
        return 10000 if self.course == "python" else 20000

    def getdue(self):
        return self.getfee() - self.feepaid

    def getcourse(self):
        return self.course



s = Student(1, "Andy", "ds")
s.payment(4000)
print(s.getdue())
