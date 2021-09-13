# ! Sum of N Natural Numbers
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)


n = int(input("Enter a number: "))
print(sum(n))

# ! Factorial of a number


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


n = int(input("Enter a number: "))
print(fact(n))
