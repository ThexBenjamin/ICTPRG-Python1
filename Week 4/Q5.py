sum = 0
num = int (input("please insert some numbers (Press x to stop) "))
while (num != ""):
    sum=sum+int(num)
    num = input("please insert some numbers (Press x to stop) ")
print (sum)