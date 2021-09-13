'''
You are given an array A of size N that contains integers. Here, N is an even number. You are required to perform the following operations:

Divide the array of numbers in two equal halves
Note: Here, two equal parts of a test case are created by dividing the array into two equal parts.
Take the first digit of the numbers that are available in the first half of the array (first 50% of the test case)
Take the last digit of the numbers that are available in the second half of the array (second 50% of the test case)
Generate a number by using the digits that have been selected in the above steps
Your task is to determine whether the newly-generated number is divisible by 11.

Input format

First line: A single integer N denoting the size of array A
Second line: N space-separated integers denoting the elements of array A 
Output format
If the newly-generated number is divisible by 11, then print OUI. Otherwise, print NON.
'''


def solve(A):
    # Write your code here
    A = list(A)
    a1 = []
    a2 = []
    for i in range(len(A)):
        if i >= len(A)/2:
            a2.append(A[i])
        else:
            a1.append(A[i])
    a1_first = []
    for i in a1:
        while i >= 10:
            i = i//10
        a1_first.append(i)
    a2_last = [a2[i] % 10 for i in range(len(a2))]
    a = a1_first + a2_last
    a = list(map(str, a))
    a = ''.join(a)
    a = int(a)
    if a % 11 == 0:
        A = 'OUI'
    else:
        A = 'NON'
    return A


N = int(input())
A = map(int, input().split())

out_ = solve(A)
print(out_)
