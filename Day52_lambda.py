# def double(x):
#     return x * 2

double = lambda x : x * 2
squer = lambda x : x *x
cube = lambda x : x * x * x
avg = lambda x , y , z : (x + y + z )/3


mul = lambda x , y : print(f"This is multiplication : {x} * {y} = {x * y}")
print("this is double ",double(2))
print("this is cube ",cube(3)) 
print("this is a squer ",squer(10))
print("this is a average ",avg(1 , 2 ,3))

mul(3 , 6)