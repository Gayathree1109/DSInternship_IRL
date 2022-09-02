# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque
a = deque()
n = int(input())

for i in range(n):
    b = input().split()
    if(b[0] == 'append'):
        a.append(b[1])
    elif(b[0] == 'popleft'):
        a.popleft()
    elif(b[0] == 'appendleft'):
        a.appendleft(b[1])
    elif(b[0] == 'pop'):
        a.pop()

print(' '.join(a))
