# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

def a(b):
    if b.group(1) == '&&':
        return 'and'
    else:
        return 'or'

for _ in range(int(input())):
    print(re.sub(r"(?<= )(\|\||&&)(?= )", a,input()))
    
    