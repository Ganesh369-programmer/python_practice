# this seek() funtion is use for move the reading position to another postion 
with open ('myfile2.txt' , 'r') as f:
    f.seek(10)
    data = f.read(10)
    print(data)



# this tell() function is use for find the current position 
with open ('myfile2.txt' , 'r') as f:
    f.read(10)
    current = f.tell()
    f.seek(current)
    data = f.read()
    print(data)


# this trucate() function is use for delete some specific data
with open('myfile2.txt' , 'r') as f:
    f.write('Hello world ')
    f.trucate(2)

with open('myfile2.txt' , 'r') as f:
    print(f.read())