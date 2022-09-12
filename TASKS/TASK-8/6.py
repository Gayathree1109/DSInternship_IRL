# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
def clt(x, m, s):
    return 1/2*(1+math.erf((x-m) / s / 2**(1/2)))
m = 2.4
s = 2
n = 100
t = 250
ms = n * m
ss = s * n**(1/2)

# Find the probability that sum <= 250
print(round(clt(t, ms, ss), 4))