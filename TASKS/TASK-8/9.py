# Enter your code here. Read input from STDIN. Print output to STDOUT

X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]

n = 5
sx = sum(X)
x = sx / n
sy = sum(Y)
y = sy / n
ss = sum([i ** 2 for i in X])
xy = sum([i * j for i, j in zip(X, Y)])

a = (n * xy) - (sx * sy)
b = (n * ss) - (sx ** 2)
c = a / b
d = y - (c * x)

p = 80
print(round(d + (c * p), 3))

