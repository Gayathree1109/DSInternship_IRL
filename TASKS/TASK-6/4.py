import numpy
n,m,p=map(int,input().split())

a1=[list(map(int,input().split())) for i in range(n)]
a2=[list(map(int,input().split())) for i in range(m)]
b1=numpy.array(a1)
b2=numpy.array(a2)

print(numpy.concatenate((a1,a2),axis=0))


