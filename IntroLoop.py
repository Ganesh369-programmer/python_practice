#for loop 

# name = "Tarkshakti"
# alph = '\n ABCDEFGHIJKLMNOPQRSTUVWXYZ '

# for i in name:
#     print(i , end= ",")

# for i in alph:
#     print(i)



#itrating Over a List 
flower = ["rose" , "sunflower" , "jaswand" , "red " , "green" , "blue"]
for x in flower:
    print(x , end=",")        

print("\n")
print("if you want use for loop then click 1 and 2")
print("if you want use while loop then click on 3 and 4")
print("use do while loop ")
x = int(input(" enter number "))



match x:
     case 1:
            for i in range(10):
                print(i , end=",")

     case 2:
            nm = "Shree Krishna "
            for a in nm:
                print(a, end=",")
         
            print("")
            str = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
            for i in str:
                  print(i, end =",")
            

     case 3:
          count = 5
          while(count > 0 ):
               print(count)
               count = count - 1
     case 4:
          print("Else with while loop ")
          x = 5
          while(x > 0):
               print(x)
               x = x - 1

          else:
            print("here x is 0")

     case 5:
          
          while(True):
               n = int(input("Enter positive number "))
               print(n)
               if(not n > 0):
                    break


                

               
          
          
               
        

          
          
