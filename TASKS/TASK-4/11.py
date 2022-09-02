def print_rangoli(size):
    # your code goes here
    import string
    a = string.ascii_lowercase
    li = []
    for i in range(n):
        b = "-".join(a[i:n])
        li.append((b[::-1]+b[1:]).center(4*n-3, "-"))
        
    print('\n'.join(li[:0:-1]+li))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)