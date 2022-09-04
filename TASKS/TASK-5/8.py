# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

a = int(input())

for i in range(a):
    n = input()
    if(len(n)==10 and n.isdigit()):
        o = re.findall(r"^[789]\d{9}$",n)
        if(len(o)==1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")