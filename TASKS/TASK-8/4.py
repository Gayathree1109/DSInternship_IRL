# Enter your code here. Read input from STDIN. Print output to STDOUT



import math
def nd(a, m, s):
    return 1/2*(1+math.erf((a-m) / s / 2**(1/2)))
m = 70
s = 10
print(round((1 - nd(80, m, s))*100, 2))
print(round((1 - nd(60, m, s))*100, 2))
print(round(nd(60, m, s)*100, 2))