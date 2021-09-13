num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
num4 = int(input("Enter 4th number: "))
if num1 > num2:
    x = num1
else:
    x = num2
if num3 > num4:
    y = num3
else:
    y = num4
if x > y:
    print("greatest is:", x)
else:
    print("greatest is:", y)
