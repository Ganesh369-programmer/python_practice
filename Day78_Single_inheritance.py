class animal:
    def __init__(self , name , species):
        self.name = name 
        self.species = species

    def animal_sound(self):
        print("sound made by animal ")

class Dog(animal):
    def __init__(self , name , breed):
        self.name = name
        self.breed = breed

    def make_sound(self):
        print("Bark!!")

class cat(animal):
    def __init__(self , name , breed):
        animal.__init__(self, name , species="cat")
        self.breed = breed

    def make_sound(self):
        print("Meo meo")
        
        
a = animal("Dog" , "Dog")

d = Dog("Raju Bhai" , "bulldog")
d.make_sound()
d.animal_sound()
c = cat("bokaa" , "janglee billa ")
c.make_sound()

