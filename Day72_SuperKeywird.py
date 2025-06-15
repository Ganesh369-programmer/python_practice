class parentclass:
    def parent_method(self):
        print("this is a parent method")

class childclass(parentclass):
    def child_method(self):
        super().parent_method()
        print("This is a child class ")

ch1 = childclass()
ch1.child_method()

#########################################################
#this is multiple inheritance
class parentclass1:
    def parent_method(self):
        print("parent method from parent class1")

class parentclass2:
    def parent_method(self):
        print("This is second parent method ")

class childclass(parentclass1 , parentclass2):
    def child_method(self):
        print("Child method")
        super().parent_method()
        
ch2 = childclass()
ch2.child_method()

#########################################################

class employee:
    def __init__(self , name , age ):
        self.name = name 
        self.age = age
        

class programmer(employee):
    def __init__(self, name , age , language):
        super().__init__(name , age)
        self.language = language
        print(f"My name is {self.name} and age is {self.age}")

        print(f"My name is {self.name} and age is {self.age} and i am trying to learn the {self.language}")

p1 = programmer("Ganesh" , 35 , "python")
e1 = employee("Harry" , 40)
print(f"My name is {e1.name} and age is {e1.age}")


