import math
sec_num =9
guess_num = 0
guess_count =3 
while guess_num< guess_count:
        guess_number = int(input("Guess a number:"))
        guess_num+=1
        if guess_number == sec_num:
         print("You guessed it right!")
         break
else:
     print("you lose!")        



