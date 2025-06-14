import random 

# for i in range(1):
#     print(random.choice(0 , 3))

# for i in range(1):
#     random.seed(0)
#     print(random.randint(0 , 3))

# num = 0

#her we trying to use a lambda function // lambda function gives some difficulties so use normal fuction
x = 0  
def num():    
    global x
    x = x + 1
    return x



def num_minus():
    global x  #here i use global variable because compliler gives error the x is local variable
    x = x - 1
    if(x < 0):  # if point value is less than 0 ( in minus ) so then give the 0 value
        x = 0
    return x



while True:
    use = int(input("Enter value \n Snack = 0 \n water = 1 \n Gun  = 2  \n Choose a value : "))

    # for i in range(3):
    #     for j in range(3):
    def comp(x):
        match x:
            case 0 :
                value = "Computer is chooses a snack"
                return value
                
            case 1:
                value = "Computer is chooses a Water"
                return value
            case 2:
                value = "computer is chooses a Gun"
                return value
            


    #this section is for computer 
    n = [0 , 1 , 2]
    computer = random.choice(n)
    print(f"{comp(computer)}")

    

    if(use == computer):
        print("The match is draw ")
        
        print(f"Your Point is {x}")  # here we use a x not a funtion because when we call a function then it is get increased
    
    if use == 69:
        break
    
    #instead of using a (if else) we can use a (match case) method
    if(use != computer):
        if((use == 0 ) and (computer == 1)):
            print("Hooorrraaay !!! We win . Snack drinks the water  ")
            # num = num + 1
            print(f"Your Point is {num()}")
            
            

        elif((use == 0) and (computer == 2)):
            print("shit !!!Here we Go again . Gun kills the snack you loss")
            # num = num - 1
            print(f"Your Point is {num_minus()}")
            

        elif((use == 1) and (computer == 0)):
            print("shit !!!Here we Go again . You loose beacuse Snack drink water ")
            # num = num - 1
            print(f"Your Point is {num_minus()}")
                
            

        elif((use == 1) and (computer == 2)):
            print("Hooorrraaay !!! You win because Water destroy the gun")
            # num = num + 1
            print(f"Your Point is {num()}")
        
        elif((use == 2) and (computer == 0)):
            print("Hooorrraaay !!! You win because Gun kills the snack ")
            # num = num + 1
            print(f"Your Point is {num()}")

        elif((use == 2) and (computer == 1)):
            print("shit !!!Here we Go again . You loss because Water destroy the gun")
            # num = num - 1
            print(f"Your Point is {num_minus()}")
                
            
        
        else :
            print("Invalid statement")


    




