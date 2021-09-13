import random
r = random.randint(1, 100)
score = 0
user = None
while(user != r):
    user = int(input("Guess the Number: "))
    score += 1
    if(user == r):
        print("You guessed it Right")
    else:
        if(user > r):
            print("Guess Smaller")
        else:
            print("Guess Larger")
print(score)
with open('hiscore.txt') as f:
    pre = int(f.read())
if pre > score:
    with open('hiscore.txt', 'w') as f:
        f.write(str(score))
    print("You Scored Highest")
else:
    print("Your Score is Lower than Previous")
