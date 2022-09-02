# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    a = int(input())
    A = set(map(int, input().split()))
    b = int(input())
    B = set(map(int, input().split()))
    if len(A - B) == 0:
        print("True")
    else:
        print("False")