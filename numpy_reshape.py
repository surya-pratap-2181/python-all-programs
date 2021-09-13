'''You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.'''
import numpy
n = input().strip().split()
n = list(map(int, n))
arr = numpy.array(n)
print(numpy.reshape(arr, (3, 3)))
