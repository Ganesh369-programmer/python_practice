

ceo_username = "ceo"
ceo_pass= 12345

aunty_username = "aunty123"
aunty_pass = 123

mahatari_username = "mahatari"
mahatari_pass = 9876


class ceo :
    def __init__(self , name ,chugali):
        self.name = name 
        self.chugali = chugali
        

    def show_detail(self):
        print(f"Name :- {self.name}")
        print(f"chugali of that person :{ self.chugali}")

class aunty(ceo):
    def __init__(self , name , chugali):
        super().__init__(name , chugali)
        super().show_detail()
    # super().show_detail()

class mahatari(ceo):
    def __init__(self , name , chugali):
        super().__init__(name , chugali)
        super().show_detail()
    # super().show_detail()


def n1():
    n = input("Enter the name of person ")
    return n 

def ch1():
    ch = input("Enter the chugali ")
    return ch


while True:
    username = input("Enter the username ")
    password = int(input("enter the password "))

    if (username == aunty_username and password == aunty_pass):

        n = n1()
        ch = ch1()
        a = aunty(n , ch)
        # a.show_detail()
    elif(username == mahatari_username and password == mahatari_pass):
        n = n1()
        ch = ch1()
        m = mahatari(n , ch)
        # m.show_detail()
    elif(username == ceo_username and password == ceo_pass):
        n = n1()
        ch = ch1()
        c = ceo(n , ch)
        c.show_detail() 
        a.show_detail() 
        m.show_detail()
    elif(username == "quite" ):
        break
    else:
        print("no you cant access ")





