# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

a, b = input(), input()
c = re.finditer(r'(?=(' + b + '))', a)

d = False
for i in c:
    d = True
    print((i.start(1), i.end(1) - 1))

if d == False:
    print((-1, -1))
    
    
    
    