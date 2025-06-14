##############################################
class myclass:
    class_variable = 0
    def __init__(self):
        myclass.class_variable += 1

    def print_class_variable(self):
        print(myclass.class_variable)

ob = myclass()
ob.print_class_variable() 


##############################################
class myclass2:
    def __init__(self , name):
        self.name = name

    def print_name(self):
        print(self.name)

ob1 = myclass2("Johan")
ob2 = myclass2("Ram")
ob1.print_name()
ob2.print_name()


##############################################

class employee:
    #class variable
    companyname = 'apple'
    noofemployee = 0

    def __init__(self , name ):
        #instance variable
        self.name = name
        self.raise_amount = 0.02
        employee.noofemployee += 1

    def showdetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.companyname} is {self.raise_amount}")

emp1 = employee("Harry")
emp1.showdetails()
emp1.raise_amount = 0.03
emp1.companyname = "apple India "
emp1.showdetails()

# this is accessing class variable
employee.companyname = "Google" 
print(f"The name of the employee is  and the raise amount in {employee.companyname} is {employee.noofemployee}")
emp1.showdetails()

emp2 = employee("Rohan")
emp2.companyname = 'nestle'
emp2.showdetails()

