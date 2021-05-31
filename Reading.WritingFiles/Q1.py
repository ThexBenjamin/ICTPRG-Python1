#Ask user for two numbers

num1 = int (input ("Enter first number: "))

num2 = int (input ("Enter the second number: ")) 

#Add both numbers together
total = num1+num2

#Outputting the response to a text file called maths
math = open ("maths.txt", "w")

math.write (str(total))

math.close()         
