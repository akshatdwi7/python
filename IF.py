import math
price  = 1000000
is_has_goodc = True
if is_has_goodc:
    price = price * 0.10
    print(" your down payment will be " ,math.floor(price) , "$")
else:
    price = price * 0.20
    print("you dont have good credit so your down payment will br ", math.ceil(price) , "$")
 


numbers = [5,2,5,2,2]
for x_count in numbers:
    output=''
    for count in range(x_count):
        output += 'x'
    print(output)


  