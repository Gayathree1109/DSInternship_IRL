def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        a = str(i)
        b = oct(i)[2:]
        c = hex(i)[2:].upper()
        d = bin(i)[2:]

        print(a.rjust(width),b.rjust(width),c.rjust(width),d.rjust(width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)