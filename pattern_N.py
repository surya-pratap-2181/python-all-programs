n = int(input("Enter rows: "))
for row in range(1, n+1):
    for col in range(1, n+1):
        if (row == col):
            print('*', end='')
        elif(col == 1 or col == n):
            print('*', end='')
        else:
            print(' ', end='')
    print()
