n = int(input("Enter rows: "))
for row in range(1, n+1):
    for col in range(1, n+1):
        if (row == col):
            print('* ', end='')
        elif(row+col == n+1):
            print('* ', end='')
        else:
            # if two spaces here then single space while printing star
            print('  ', end='')
    print()
