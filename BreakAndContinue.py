for i in range(1, 101,1):
    print(i, end=",")

    if(i == 15):
        break #it is specially use for brake the loop 
    else:
        print("mission")


print("")
print("")
for i in [1,2,3,4,5,6,7,8,9,10]:
    #print(i , end=",")

    if(i % 2 == 0):
        continue #it is specially use for skip one iteration of loop

    print(i)