# import random
# import string

# #Ask user what their full name and age is
# user = input("Please enter your first name: ")
# name = input("Enter your last name: ")
# age = int(input("Enter your age: ")) 


    
# #Plus 6 to their age
# print ("Your new age is:", (age + 6))


# #Output a seperated email and password using '|'
# def random_let(y):
#        return ''.join(random.choice(string.ascii_letters) for x in range(y))
# def random_num(y):
#        return ''.join(random.choice(random.choice(string.digits)) for x in range(y))
# print (user+ name+ random_num(2) + "@Huawow.io""|"+ (random_let(8) + random_num(2)))

n = 5
while n > 0:
       n = n-1
       if n == 2:
              break
       print(n)
print ('All done here')
