class Course:
    # constructor
    def __init__(self, title, fee=10000):
        # Object attributes
        self.title = title
        self.fee = fee

    # Methods
    def getnetfee(self):
        return self.fee + self.fee * 12 // 100

    def settitle(self, newtitle):
        self.title = newtitle


c1 = Course("Python")  # create an object
c1.settitle("Python 3.12")
print(c1.title)
print(c1.getnetfee())
c2 = Course(fee=5000, title="React")
