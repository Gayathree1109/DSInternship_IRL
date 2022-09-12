# Enter your code here. Read input from STDIN. Print output to STDOUT

a, b = 500, 80
c, d = a, b/(100**0.5)
e = a - (1.96*d)
f = a + (1.96*d)

print(round(e,2))
print(round(f,2))