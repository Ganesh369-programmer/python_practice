class detail:
       
    def __init__(self):
        '''This  is Default constructor '''
        print("This is out first code of our constructor  ")

    
    def c(self):
        '''This is code of Default constructor '''
    

o = detail()
o.c()


def a():
    an = []
    n = int(input("Enter the number of animal"))
    for i in range(n):
        janwar = input("Enter the name of animal")
        an.append(janwar)
    return an
    
def g():
    gp = []
    n = int(input("Enter the number of group"))
    for i in range(n):
        group = input("Enter the name of animal")
        gp.append(group)
    return gp

class environment:

    def __init__(self , animal , group):
        self.animal = animal
        self.group = group
        # print(f"{self.animal} is belongs to {self.group}")

    def display(self):
        for x in range(len(self.animal)):
            print(f"{self.animal[x].capitalize()} is from this {self.group[x]} Group") #this is shortest form of mylogic we can show both output by using this 

        #we doesnt need to run this code just like this 
        # for x in range(len(self.animal)):
        #     print(f"\n {self.animal[x]}")
        #     for y in self.group[x]:
        #         print(f" and {y}")

    

# animal = ['a' , 'b' , 'c' , 'd']
# group = ['a' , 'b' , 'c' , 'd']
animal = a()
group = g()
ob = environment(animal , group)
ob.display()
# ob = environment("crab" , "Crustanceans")

# i = []
# y = []
# for x in range(3):
#     ij = input("Enter animal name :")
#     yj = input("Enter the group name :")
#     i.append(ij)
#     y.append(yj)


    
