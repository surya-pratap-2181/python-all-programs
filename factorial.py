num = int(input("Enter a Number to find factorial: "))
fact = 1
for i in range(1, num+1):
    fact = fact*i
print("Factorial is: ", fact)
