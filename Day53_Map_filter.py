from functools import reduce 
def cube(x):
    return x * x * x

print(cube(2))

l = [1 , 2 ,3 , 4 ,5 ,6]
newl = []
for item in l:
    newl.append(cube(item))

print(newl)

# this is map() function is use 
newl = list(map(cube , l))
print(newl)



# this is use for finding a cube of number
n = []
i = int(input("Enter the number "))
for x in range(i):
    n.append(x)
    # print(n)
num = list(map(cube, n))
print("This is a cube ",num)


num = [1 , 2 , 3 ,4 ,5 , 6]
#this filter function is use for filter the value , if value is true then it returns the value 
even = filter(lambda x : x % 2 == 0 , n)
print("this is a even ",list(even))

#this is return a one value 
sum = reduce(lambda x , y : x + y , n)
print(sum)
