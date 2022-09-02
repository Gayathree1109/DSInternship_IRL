if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = []
    for i in arr:
        if i not in a:
            a.append(i)
            
    b = sorted(a)
    print(b[-2])
    