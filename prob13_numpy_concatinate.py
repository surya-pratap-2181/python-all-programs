'''
Task

You are given two integer arrays of size NxP and MxP (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.

Input Format

The first line contains space separated integers N, M and P.
The next N lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.

Output Format

Print the concatenated array of size (N+M)xP.
'''
import numpy

N, M, P = map(int, input().split())
ar1 = numpy.array([input().strip().split() for _ in range(N)], int)
ar2 = numpy.array([input().strip().split() for _ in range(M)], int)
print(ar1)
print(ar2)
print(numpy.concatenate((ar1, ar2), axis=0))
