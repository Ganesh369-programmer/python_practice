## this is use for read the data in file
# f = open('myfile.txt' , 'r')
# while True:
#     line = f.readline()
#     if(not line):
#         break
#     print(line)


## This is use for write the data in a file 
# f1 = open('myfile.txt' , 'w')
# # line1 = [ 'line 1 \n ', ' line 2 \n' , 'line 3 \n ']
# line1 = input("Enter anything you want ")    #by using this you can add anything data in your file 

# f1.writelines(line1)
# f1.close()


##for loop is use for writing a data
# f = open('myfile.txt' , 'w')
# lines = ['lines' , 'lines1' , 'lines2']
# for line in lines:
#     f.write(line +"\n")

# f.close()


f = open('myfile.txt' , 'r')
i =0 
while True :
    i = i + 1
    line = f.readline()
    if not line:
        break

    m1 = int(line.split(',')[0])
    m2 = int(line.split(',')[1])
    m3 =int(line.split(',')[2])

    print(f"mark of student {i} in math is : {m1} ")
    print(f"mark of {i} in english {m2}")
    print(f"mark of std {i} in sst is : {m3}")


    #print(line)