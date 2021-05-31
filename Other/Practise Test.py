import random

num = random.randint(1, 25)

log = [] 

count = 1

print ("Guess the number between 1 and 25")

print ("Be wise, you only have 7 guesses")

user = int(input("What's the number? "))
log.append(user)

while user != num:
    
    

    if user > num:
     print ("Lower")
     print("Guesses remaining: ", 7 - count)
     

    elif user < num:
     print ("Higher")
     print("Guesses remaining: ", 7 - count) 
    

    user = int(input("What's the number? "))

    count += 1
    
    log.append(user)

    if num == user:
        break
    
    elif count == 7:
        print ("You ran out of guesses you fool")
        print ("The number was", num)
        print ("Your guess log:\n", log)
        input ("Press enter to exit")
        exit()

print("You got it!, the number is", num, "and it only"\
       " took you", count , "tries")
print ("Your guess log:\n", log)

input ("Press enter to exit")
