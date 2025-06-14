def name(fname , mname = "john" , lname = "wick"): #here we use default names
    print("Hello", fname , mname , lname )

name("amy" , "raju " , "ketu")


def name(fname , mname , lname ):
    print("Hello ", fname , mname , lname)

name(mname="s" , fname="a " , lname="b")
name(fname="a" , mname="b" , lname= "c")


#Arbitary Argument 
def name(*name):
    print("\n Here the arbitary argument are used ")
    print("Hello ,", name[0] , name[1] , name[2])

name("James ", "b" , "c")

#keyword Arbitary argument 
def name(**name):
    print("\n Here the keyword arbitary argument are used ")
    print("Hello , ", name["fname"] , name["mname"] , name["lname"] , name["gname"] , name["pname"])

name(fname = "Ganu" , mname = "ramu" , lname = "shyamu", gname = "g" , pname = "p")



#example
def average(*number):
    sum = 0
    for i in number:
        sum = sum + i

    return sum/len(number)
    #print("Average is :", sum/len(number))
        
c = average(1,2,3,4,5,6,7,8)
print(c)

