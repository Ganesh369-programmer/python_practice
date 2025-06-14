#this code throws the error because we cant run the code in on private vaiable and method
# class student:
#     def __init__(self , age , name ):
#         self.__age = age
        
#         def __funname(self):
#             self.y = 34
#             print(self.y)


# class subject(student):
#     pass

# obj = subject(21, "Ganesh")
# print(obj.__age)
# print(obj.__funname())


class myclass:
    def __init__(self):
        self._nonmangled = "this is nonmangled attribute"
        self.__mangled = "this mangled attribute "


my = myclass()
print(my._nonmangled)
# print(my.__mangled)
print(my._myclass__mangled)


