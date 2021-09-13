import time
import random


def game(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        else:
            return False
    elif comp == 'p':
        if you == 's':
            return True
        else:
            return False
    elif comp == 's':
        if you == 'r':
            return True
        else:
            return False


print("*************************************")
print("Rock Paper Scissor")
print("*************************************\n\n")
print("Computer's Turn: ")
time.sleep(1)
comp = random.randint(1, 3)
if comp == 1:
    comp = 'r'
elif comp == 2:
    comp = 'p'
elif comp == 3:
    comp = 's'
# print(comp)
print()
you = input("Your Turn: ")
# print(you)
result = game(comp, you)
if result == None:
    print("It's a tie")
elif result:
    print("You Won")
else:
    print("You Lose")
print("Computer Chosed", comp)
print("You Chosed", you)
