'''
You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

'''
import numpy
c = list(map(int, input().strip().split()))
print(numpy.zeros(c, int))
print(numpy.ones(c, int))
