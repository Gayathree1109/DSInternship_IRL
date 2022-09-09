import numpy

A, B = map(int, input().split())
storage = numpy.array([input().split() for _ in range(B)],int)
print(numpy.max(numpy.min(storage, axis=1), axis=0))



