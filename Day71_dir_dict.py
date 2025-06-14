x = [1 , 2 , 3]
print(dir(x))  #this is use which type of method is used on that object

b = (2 , 3 , 4)
print(dir(b))


class person:
    def __init__(self , name , age):
        self.name = name 
        self.age = age

p = person("john" , 30)
print(f"\nThis is dict method {p.__dict__}")

print(help(p))