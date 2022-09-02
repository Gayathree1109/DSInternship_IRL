def merge_the_tools(string, k):
    # your code goes here
    a = []
    b = 0
    for i in string:
        b = b + 1
        if i not in a:
            a.append(i)
        if b == k:
            print (''.join(a))
            a = []
            b = 0
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)