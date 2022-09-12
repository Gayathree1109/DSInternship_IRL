# Enter your code here. Read input from STDIN. Print output to STDOUT


n = int(input())
x = list(map(float,input().strip().split()))
y = list(map(float,input().strip().split()))
a = sum(x) / n
b = sum(y) / n
sx = (sum([(i - a)**2 for i in x]) / n)**0.5
sy = (sum([(i - b)**2 for i in y]) / n)**0.5
c = sum([(x[i] - a) * (y[i] - b) for i in range(n)])
cc = c / (n * sx * sy)
print(round(cc,3))