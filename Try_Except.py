
# while True:

#     try:
#         num = int(input("Enter the integer :"))
#     except ValueError as e:
#         print("Number entered is not an integer ",e)

#     if(num == 0):
#         break


# a = input("Enter the number :")
# print(f"Multiplication table of {a} is: ")
# try:
#     for i in range(1,11):
#         print(f"{int (a)} x {i} = {int (a) * i} ")
# except:
#     print("invalid input ")



# try:
#     num = int(input("Enter an integer :"))
#     a = [6,3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an int ")
# except IndexError as e:
#     print("Index Error ", e)


##################################################################################################
x = [ 2 , 4 , 4, 5 , 6, 7 , 8 ]

try:
    n = int(input("enter the number :"))
    
    for i in x:
        if(i == n):
            print(f"this {n} value is available in array . at the place of this index {x.index(n)}")  #this code is use for find the integer value in list
            
            break
    else:
        print(f"{3} Value is not available in array ")


        
        
except ValueError as e:
    print(e)

finally:
    print("Your work is completed ")