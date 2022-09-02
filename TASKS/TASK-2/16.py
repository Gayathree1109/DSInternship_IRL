# Enter your code here. Read input from STDIN. Print output to STDOUT
A = int(input())
a = set(input().split())

B = int(input())
b = set(input().split())

c = a.symmetric_difference(b)

print(len(c))