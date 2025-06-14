ls = [1,2,1,2,3,2,5,3,6,8]
colors = ["red" , "green " , "blue" , "voilet"]

print(ls)

print(colors[0])
print(colors[3])
print(colors[2])

print(colors[-1])
print(colors[-2])
print(colors[-3])

if "green " in colors:
    print("The green is present ")
else:
    print("The green is absent ")


animals = ["dog" , "cat" , "hourse" , "mouse" , "lion" , "tigers" , "chitta" , "bear", "yark"]
print(animals[:7]) #print until 7 
print(animals[2:9:3]) 
print(animals[-7:-2])
print(animals[ : :3])


colors = ["red" , "voilet" , "blue" , "green" , "yellow", "green", "green", "green"]
num = [4 ,3 ,2 ,5 , 6,2,43,12,45,68,1 ,89]



print("This is the index of normal list :",colors.index("green"))
print("This is index of normal number of list :",num.index(3))

colors.sort()
print(colors)



num.sort()
print(num)

num.sort(reverse=True)
print(num)

num.reverse()
print(num)

print("This is the index of sorted list :",colors.index("green"))
print("This is index of sorted number of list :",num.index(3))

print(colors.count("green"))
print(num.count(2))


newlist = colors.copy()
newlist.insert(1,"lal hai ")
print("this is a new list :",newlist)

newlist.append("kala")
print("Here append methos is used :", newlist)

newlist.extend(colors)
print(newlist)
print(newlist + colors)  #this is use for combine the two list 









