N = int(input())
arr = []
for i in range(1, N+1):
    x = input().split()
    if('insert' in x):
        arr.insert(int(x[2]), int(x[1]))
    if(x == 'print'):
        print(arr)
    if('remove' in x):
        arr.remove(int(x[1]))
    if('append' in x):
        arr.append(int(x[1]))
    if(x == 'sort'):
        arr.sort()
    if(x == 'pop'):
        arr.pop()
    if(x == 'reverse'):
        arr.reverse()
