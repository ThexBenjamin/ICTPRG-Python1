a = 0
e = 0
name = input("Enter some random characters: ")
for i in name:
    if i =="a":
        a+=1
    elif i == "e":
        e+=1
# sent = input("Enter your text: ")
print ("a:",name.count("a"))
print ("e:",name.count("e"))