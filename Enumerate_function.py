fruits = ['apple' , 'bannana' ,'mango' , 'peru' , 'Grapes']
for i , f in enumerate(fruits , start= 1):
    print(f"{i} : {f}")

# here i = indicate the index and f is indicate the values


print('\n')
color = ( # this is a tuple 
    'red',
    'blue',
    'green',
    'yellow',
    'orange'
)

for i , f in enumerate(color):
    print(f"{i + 1} : { f }")   # here { i + 1 } act like start method of enumerate


s = "hello world"
for i, c in enumerate(s):
    print(i, c)


