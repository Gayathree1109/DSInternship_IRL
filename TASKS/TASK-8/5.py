# Enter your code here. Read input from STDIN. Print output to STDOUT


import math
def clt(x, m, s):
    return 1/2*(1+math.erf((x-m) / s / 2**(1/2)))
m = 205
s = 15
n = 49
t = 9800
ms = n * m
ss = s * n**(1/2)
print(round(clt(t, ms, ss), 4))