# How to handle error in py 
try:
    age =int(input("your age:"))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print('Invalid value')
    