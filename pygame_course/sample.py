class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self):
        print(f"{self.name} eat up!!!")
        
    def bark(self):
        print("WOOF WOOF WOOF")
        
class Beagle(Dog):
    def __init__(self, name, age, something):
        super().__init__(name, age)
        self.something = something
        
    def hunt(self):
        print(f"{self.name} is hunting")
    
    
b1 = Beagle("jessi", 12,"bbbb")
b1.eat()
b1.bark()
b1.hunt()