num =(1,2,3)
x,y,z  = num
print(z)

#Concepts of unpacking where we don't have to assign each variable separately
#we can directly unpack the values in the tuple

#Dictionaries in PY is more like JSON 
customers ={
    "name":"Aksaht",
    "age": 21,
    "degree": "CSE",
    "mood": "Happy",
    "is_verified": True
    }

customers["dog"]="German shepard"

phone = input("Phone:") # to convert number into worldy number 
diary= {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
output=''
for yo in phone:
    output+= diary.get(yo, " !") + " "
print(output)


#2 EMOJI CONVERTER 
message = input("<")
words = message.split(' ')
print(words)