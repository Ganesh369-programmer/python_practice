class person:
    name = "Ganesh"
    age = 20


obj = person() #this is use for create the object 
print(obj.name)
print(obj.age)

class manushya:
    n = "Ganesh"
    a = 20

    def info(self):
        print(f"My name is {self.n} and my age is {self.a}")

obj2 = manushya()
obj2.info()

obj2.n = "raju"
obj2.a = 10
obj2.info()

obj3 = manushya()
obj4 = manushya()

obj3.n = "ram"
obj3.a = 20
obj4.n = "shyam"
obj4.a = 18
obj3.info()
obj4.info()