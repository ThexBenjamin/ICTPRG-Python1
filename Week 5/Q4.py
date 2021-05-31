name = input("Please enter your full name:")
fullname = name.split()
initials = ""
for i in range(len(fullname)):
    initials+=fullname[i] [0]
    print ("fullname:", name)
    print ("initials:", initials)