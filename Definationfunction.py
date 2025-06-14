def CalculateNum(a,b):
    result = (a*b)/(b/a)
    print(result)

def GreaterNumber(a,b):
    if(a>b):
        print("Here",a,"is Greater than",b) 
    else:
        print("here",b ,"is Greater than", a)


CalculateNum(2,3)
GreaterNumber(3,4)   


#here i use do while loop 
while True:
    
    x = int(input("enter the number "))
    if( x == 0):
        print("exiting The loop ")
        break

    match x:
        case 1:
          a = int(input("Enter the value of a "))
          b = int(input("enter the value of b "))
          CalculateNum(a,b)

        case 2:
          a = int(input("Enter the value of a "))
          b = int(input("enter the value of b "))
          GreaterNumber(a,b)
    
    





