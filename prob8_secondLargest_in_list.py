# i = int(input())
# lis = list(map(int, input().strip()))
# z = max(lis)
# while max(lis) == z:
#     lis.remove(max(lis))

# print(max(lis))
'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[]  of n integers each separated by a space.

'''

n = int(input())
arr = map(int, input().split())
lst = list(arr)
z = max(lst)
while max(lst) == z:
    lst.remove(max(lst))
print(max(lst))
