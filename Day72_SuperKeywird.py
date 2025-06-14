class parentclass:
    def parent_method(self):
        print("this is a parent method")

class childclass(parentclass):
    def child_method(self):
        super().parent_method()
        print("This is a child class ")

ch1 = childclass()
ch1.child_method()