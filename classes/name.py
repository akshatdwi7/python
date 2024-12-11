
class Person:  #class
    def __init__(self, name): #method 
        self.name = name 

    def talk(self):  
        print(f"{self.name} is talking")

jhon = Person("Jhon")  
jhon.talk()
#output: Jhon is talking
 