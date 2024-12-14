from pathlib import Path

#Absolute path , It is from the root of the hard disk like from ascending order 

# relaive path ,It is from currect file it goes like in decsednig order 
path =Path()
for i in path.glob('*.py'):
    print(i)