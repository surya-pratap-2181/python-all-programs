n = input("Enter string: ")
for row in range(1, len(n)+1):
    for col in range(row):
        print(n[col], end='')
    print()
