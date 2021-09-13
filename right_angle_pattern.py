for i in range(1, 5):
    for j in range(5, i, -1):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
