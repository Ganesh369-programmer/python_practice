#here use int , because here str and int 
x = int(input("enter the value "))

match x:
    case 0:
        print("the value is 0 ")
    
    case 1:
        print("the value is 1")
    
    case 2 :
        print("the value is 2")

    case 4 if x%2 == 0 :
        print("the value is 4 and if x%2 == 0")

    case _ :
        print("the value is empty")

