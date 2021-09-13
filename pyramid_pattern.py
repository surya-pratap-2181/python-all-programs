# ! Pyramid
n = int(input("enter no.: "))
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))

# ! Pyramid Upside Down
n = int(input("enter no.: "))
for i in range(n, 0, -1):
    print(" "*(n-i)+"* "*(i))
