#Ask for names until entering a blank name

#Create a file called 'people.txt'
names = open ("people.txt", "w")

while True:
        name = input('Enter a name: ')
        if name == "":
                break
        #Add names on a seperate line
        names.write (name + '\n')
             
         
names.close()   


