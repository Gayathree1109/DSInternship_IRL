# Enter your code here. Read input from STDIN. Print output to STDOUT

import math


a = 0.12
b = 0
for i in range(0, 3):
    b += math.factorial(10)/math.factorial(i)/math.factorial(10-i) * a**i * (1-a)**(10-i)
    if i == 1:
        c = 1 - b

print(round(b, 3))
print(round(c, 3))