fruit = "Mango"
alf = "abcdefghihklmnopqrstuvwxyz"
len1 = len(fruit)

print("the length of fruit ",len1)
len1 = len(alf)
print("the length of alphabet ",len1)

p = "I_am_leaning_a_python "
print("1",p[:5])
print(p[5:])
#here i combine both slicing method 
print(p[:5] + p[5:])

print
print(p[2:7])
print(p[:-8]) #slicing a negative charater
print(p[-8:]) #slicing a negative charater


#Loop throuth a string 
# for i in alf:
#     print(i)