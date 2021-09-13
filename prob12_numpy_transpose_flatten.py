'''
Task

You are given a NxM integer array matrix with space separated elements ( N= rows and  M= columns).
Your task is to print the transpose and flatten results.

Input Format

The first line contains the space separated values of N and M.
The next N lines contains the space separated elements of M columns.

Output Format

First, print the transpose array and then print the flatten.


'''
import numpy
n = input().strip().split()
x = []
for m in range(int(n[0])):
    x.append(input().strip().split())
x = numpy.array(x, int)
print(numpy.transpose(x))
print(x.flatten())

''' Shortest Solution
# import numpy
# n, m = map(int, input().split())
# array = numpy.array([input().strip().split() for _ in range(n)], int)
# print(array.transpose())
# print(array.flatten())
'''
