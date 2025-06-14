#this is Getter 
class myclass:
    def __init__(self , value , a , b ):
        self._value = value
        self.a = a
        self.b = b

    @property  #getter method is defined by using this method 
    def v(self):
        return self._value , self.a , self.b  #by using getter we can provide more than one value
    

    @v.setter
    def v_setter(self , new_value ):
        self._value , self.a , self.b = new_value  #by using this technique we can use multiple value for setter
        # self.a = a
        # self.b = b

obj = myclass(10 , 20 , 30 )
print(f"Before{obj.v}")

obj.v_setter = (20 , 30 , 40)

print(f"After{obj.v_setter}")
  