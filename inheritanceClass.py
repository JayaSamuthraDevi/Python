class Animal:

    def __init__(self):
        self.eyes=2
    
    def move(self):
        print("Moving")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        

    def bark(self):
        print("Barking")


d=Dog()

print(d.eyes)
d.move()
d.bark()
