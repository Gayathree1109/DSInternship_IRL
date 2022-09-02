# Enter your code here. Read input from STDIN. Print output to STDOUT
n_m = map(int, input().split())
n = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

ih = 0

for i in n:
    if i in A:
        ih = ih+1
    elif i in B:
        ih = ih-1
print(ih)
        

 