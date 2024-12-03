weight =int(input(" What is your weigth ? "))

unit =input(("is it K(g) OR L(b) ?"))
if unit.upper() == "L":
    converted= weight * 0.45
    print(f"your weight in kg is {converted} kg")
else:
    converted = weight / 0.45
    print(f"your weight in lbs is {converted} lbs")  # this is the same
