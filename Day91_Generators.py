a = lambda x : x *x 

def my_generators():
    for i in range(5):
        yield i

gen = my_generators()
print(next(gen))
print(next(gen))
print(next(gen))

