# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
n = int(input())
for t in range(n):
    c1 = input().strip()
    c = c1.replace('-','')
    a = True
    l1 = bool(re.match(r'^[4-6]\d{15}$',c1))
    l2 = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$',c1))    
    consecutive = bool(re.findall(r'(?=(\d)\1\1\1)',c))
    if l1 == True or l2 == True:
        if consecutive == True:
            a=False
    else:
        a = False       
    if a == True:
        print('Valid')
    else:
        print('Invalid')