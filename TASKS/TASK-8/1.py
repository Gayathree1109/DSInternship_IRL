# Enter your code here. Read input from STDIN. Print output to STDOUT

def a(n):
    return 1 if n == 0 else n*a(n-1)

def b(n, c):
    return a(n) / (a(c) * a(n-c))

def g(c, n, p):
    return b(n, c) * p**c * (1-p)**(n-c)

d, e = list(map(float, input().split(" ")))
f = d / e
print(round(sum([g(i, 6, f / (1 + f)) for i in range(3, 7)]), 3))