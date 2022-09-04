# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

s = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(), re.IGNORECASE)

if s:
    for a in s:
        print(a)
else:
    print(-1)
    
    