# Enter your code here. Read input from STDIN. Print output to STDOUT

p = set(input().split())
a = True
for i in range(int(input())):
    q = set(input().split())
    if (p > q) == False:
        a = False
        break
print(a)
