class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    def printname(self):
        print(self.firstName, self.lastName)
class Student(Person):
    def __init__(self,firstName,lastName,gradYear):
        super().__init__(firstName,lastName)
        self.gradYear = gradYear
    def welcomeSelf(self):
        print(f"Welcome {self.firstName} {self.lastName}! to the class of {self.gradYear} student")

x = Student("Ashish", "Smith", 2025)
x.printname()
x.welcomeSelf()