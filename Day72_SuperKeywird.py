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
    def __init__(self , name , id ):
        self.name = name
        self.id = id


class programmer(employee):
    def __init__(self, name, id , lang):
        self.lang = lang
        super().__init__(name, id)

rohan = employee("Ganesh pawar" , 420)
harry = programmer("harry" , "2345" , "Python")

print(harry.name)
print(rohan.name)