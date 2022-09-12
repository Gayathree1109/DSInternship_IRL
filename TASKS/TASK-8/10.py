# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
from numpy.linalg import inv
m,n = map(int,input().split())
x,y = [],[]
for _ in range(n):
    line = list(map(float,input().split()))
    line.insert(0,1)
    x.append(line[:-1])
    y.append(line[-1])

X = np.array(x)
Y = np.array(y).T
B = inv(X.T @ X) @ X.T @ Y
       
q = int(input())
for _ in range(q):
    row = list(map(float,input().split()))
    row.insert(0,1)
    Xq = np.array(row)
    print(Xq @ B)