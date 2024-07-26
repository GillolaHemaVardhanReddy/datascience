# inheritance is a way to inherit all methods and attributes from parent class
# not only inherit we can also create new methods and attributes
# syntax:
# class Child(Parent):
    # def __init__(self):
        # super.__init__()
# here everything in Parent class is available to child class

class Animal:
    def __init__(self):
        self.num_eyes = 2
        self.num_legs = 4
    def breath(self):
        print("inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__() # this will help inherit all the methods and attributes
        self.num_fins = 6
    def swim(self):
        print("fish can swim")
    def breath(self):
        super().breath()
        print("doing this underwater")

nemo = Fish()
nemo.breath() # method from parent class
nemo.swim() # method of its own
print("attribute from parent class: ",nemo.num_eyes)
print("attribute from its own: ",nemo.num_fins)