import random

class Dice:
    def roll(self):
       firstnum= random.randint(1, 6)
       secondnum =random.randint(1,6)
       return firstnum,secondnum
    

dice =Dice()
print(dice.roll())