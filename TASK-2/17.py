# Enter your code here. Read input from STDIN. Print output to STDOUT

A = int(input())
B = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    a = input().split()
    n = set(map(int, input().split()))
    eval('B.{}({})'.format(a[0], n))
print(sum(B))