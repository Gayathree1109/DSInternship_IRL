# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

for i in range(int(input())):
    n = input().strip()
    if n.isalnum() and len(n) == 10:
        if bool(re.search(r'(.*[A-Z]){2,}',n)) and bool(re.search(r'(.*[0-9]){3,}',n)):
            if re.search(r'.*(.).*\1+.*',n):
                print('Invalid')
            else:
                print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')
