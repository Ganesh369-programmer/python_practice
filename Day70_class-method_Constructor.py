class rectangle:
    def __init__(self , width , height):
        self.width = width
        self.height = height
        print(height*width)
        


    @classmethod
    def square(cls , size):
        return cls (size , size)
    
rec = rectangle.square(10)

##############################################

class employee:
    def __init__(self , name , salary):
        self.name = name 
        self.salary = salary

    @classmethod
    def strfrom(cls , string):
        return cls(string.split("-")[0] , int(string.split("-")[1]))
    

e1 = employee("harry" , 2000)
print(e1.name , e1.salary)

str = "Ganesh-2005"
gtr = "GTA-6"
e2 = employee.strfrom(str)
print(e2.name , e2.salary)
e2 = employee.strfrom(gtr)
print(e2.name , e2.salary)

##############################################

class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    @classmethod
    def fromstring(cls , string):
        name , age = string.split(",")
        return cls(name , int(age))

s = "Ganesh, 2005"   
p1 = person.fromstring(s)
print(p1.name , p1.age)




