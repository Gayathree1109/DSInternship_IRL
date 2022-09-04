# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

t = int(input())
c = False
for _ in range(t):
    s = input()
    if '{' in s:
        c = True
    elif '}' in s:
        c = False
    elif c:
        for co in re.findall('#[0-9a-fA-F]{3,6}', s):
            print(co)