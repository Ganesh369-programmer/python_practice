class Employee:
    def __init__(self ,name , age):
        self.name = name
        self.age = age

    def showdetails(self):
        print(f"The Employee name is {self.name} and age is {self.age}")

class person(Employee):
    def show(self):
        print("Python is best language")

e1 = Employee("Ganehs" , 20)
e1.showdetails()

e2 = person("Harry" , 40)
e2.showdetails()
e2.show()