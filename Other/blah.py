# import random
# import string

# def random_char(y):
#        return ''.join(random.choice(string.ascii_letters) for x in range(y))

# print (random_char(7)+"@gmail.com")

# # import string
# # import random

# # symbols = ['*', '%', '£'] # Can add more

# # password = ""
# # for _ in range(9):
# #     password += random.choice(string.ascii_lowercase)
# # password += random.choice(string.ascii_uppercase)
# # password += random.choice(string.digits)
# # password += random.choice(symbols)
# # print(password)
# keep_going = True

# names = open ('people.txt', 'w')

# while keep_going is True:
#   name = input ('enter names: ')
#   if name == '':
#     keep_going = False
#     break
# else:
#   names.write (str(name))

user = input("Please enter your first name: ")
print (user.title())