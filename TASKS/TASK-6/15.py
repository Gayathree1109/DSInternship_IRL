import numpy
a = int(input())
b = numpy.array([input().split() for _ in range(a)], float)
print(round(numpy.linalg.det(b),2))