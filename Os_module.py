import os
f = os.open("myfile.txt" , os.O_WRONLY)

# c = os.read(f , 20)
# print(c)

# os. close(f)



os.write(f,b"Hello , world ")
os.close(f)

# i = input("Enter link")
# file = os.listdir(i)
# print(file)


f = open('myfile.txt' , 'r')

content = f.read()
print(content)
