def game():
    return 59411


highscore = game()

with open('hiscore.txt') as score:
    previous = score.read()
if previous == '':
    with open('hiscore.txt', 'w') as pre:
        pre.write(str(highscore))
    print('Your Score')
elif int(previous) < highscore:
    with open('hiscore.txt', 'w') as newScore:
        newScore.write(str(highscore))
    print('You Scored Highest')
else:
    print("your Score is less than previous")
