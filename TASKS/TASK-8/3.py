# Enter your code here. Read input from STDIN. Print output to STDOUT


import math
def nd(x, m, s):
    return 1/2*(1+math.erf((x-m) / s / 2**(1/2)))
m = 20
s = 2
print(round(nd(19.5, m, s), 3))
print(round(nd(22, m, s) - nd(20, m, s), 3))