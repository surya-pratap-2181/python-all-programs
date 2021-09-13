char = 48
n = int(input("Enter no. of row:"))
# for i in range(1, n+1):
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(char+j), end='')
    print()
