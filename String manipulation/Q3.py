characters = input("Enter some characters: ")
if len(characters) > 7:
    text = slice(len(characters)//2-1, len(characters)//2+2)
    print (characters[text])