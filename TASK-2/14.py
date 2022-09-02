# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
A = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))

print(len(A.intersection(B)))
