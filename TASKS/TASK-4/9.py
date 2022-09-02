# Enter your code here. Read input from STDIN. Print output to STDOUT

B, A = map(int, input().split())
for i in range(1, B, 2):
    print((i * ".|.").center(A,"-"))
print("WELCOME".center(A, "-"))
for i in range(B-2, -1, -2):
    print((i * ".|.").center(A, "-"))  