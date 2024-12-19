class Mammal:
    def Walk(self):
        print("Mammals can walk duh!")

class Dog(Mammal):
    def Bark(self):
        print("wolf")

class Cat(Mammal):
    def Meow(self):
        print("Meow-Meow")
        

dog1 =Dog()
dog1.Bark()
dog1.Walk()