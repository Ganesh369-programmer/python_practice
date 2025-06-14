class employee:
    company = "Apple"

    def show(self):
        print(f"Name is {self.name} and {self.company} company")

    @classmethod
    def changecompany(cls , newcompany):
        cls.company = newcompany


e1 = employee()
e1.name = "Harry"
e1.show()

e1.changecompany("Google")
e1.name = "Ganesh"
e1.show()