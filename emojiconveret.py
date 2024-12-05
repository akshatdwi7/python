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
    
    print(output) # print the outputhey




    words = ['apple', 'banana', 'apple', 'orange', 'banana']
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # Output: {'apple': 2, 'banana': 2, 'orange': 1}
