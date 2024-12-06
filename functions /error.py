# How to handle error in py 
try:
    age =int(input("your age:"))
    print(age)
except ValueError:
    print('Invalid value')