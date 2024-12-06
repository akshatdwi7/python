def convert_moji(message):
    words =message.split(" ")
    emoji={
        ":)":"🥰",
        ":(":"🥲"
    }
    output=""
    for word in words:
        output+=emoji.get(word,word)+ " "
    return output


message=input("<")
print(convert_moji(message))