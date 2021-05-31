grade = int(input("What was your grade? "))
if grade <= 100 and grade >= 90:
    print ('You will recieve a High Distinction')
elif grade <= 89 and grade >= 80:
    print ('You will recieve a Distinction')
elif grade <= 79 and grade >= 70:
    print ('You will recieve a Credit')
elif grade <= 69 and grade >= 50:
    print ('You will recieve a Pass')
else:
    print ('Invalid Score, Enter score again')