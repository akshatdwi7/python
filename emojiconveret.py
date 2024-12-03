#2 EMOJI CONVERTER 
message = input(">")
words = message.split(' ') # split the message into words or rather space separated words
emojis={
    ":)": "😊",
    ":(": "😔",
}
output = ""
for word in words:
    output+= emojis.get(word,word) + " "
    
    print(output) # print the output