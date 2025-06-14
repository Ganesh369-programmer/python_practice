import logging
def log_function_call(func):
    def decorded(*args , **kwargs):
        #func.__name__ it indicate the name of function 
        #args defines the argument which is provided in a function argument means it returns the arguments
        print(f"function {func.__name__} with args = {args} , kwargs = {kwargs}")
        func(*args , **kwargs)
        result = func(*args , **kwargs)   #result returns the output of function
        print(f"{func.__name__} returned {result} ")
        return result
    return decorded


@log_function_call
def my_function(a , b):
    # print(a + b)
    return a + b
    
my_function(10 , 20)
#print(my_function(10 , 20))


def greet(fx):
    def mfx(*args , **kwargs):
        print("Good Morning ")
        fx(*args , **kwargs)
        print("Thanks for using this function ")
    return mfx

@greet
def name():
    print("Dear Ganesh")

@greet
def hello():
    print("Hello world ")

name()
hello()