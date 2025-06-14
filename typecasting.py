a = 1;
b = 2;
print( a + b)

c = "1";   # when you use a " " for numbers then python consider them a string .
d = "2";
print( c + d)

c = "1";   #so use a typecasting .
d = "2";
print( int(c) + int(d))


#Implicit type casting
a1 = 12434
a2 = 12.12
a3 = "23445"

print(type(a1))
print(type(a2))
print(type(a3))