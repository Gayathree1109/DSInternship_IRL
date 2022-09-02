# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
a = set(map(int,input().split()))
N = int(input())
b = set(map(int,input().split()))
c = a.union(b)
d = a.intersection(b)
e = sorted(list(c-d))
for i in e:
    print(i)

