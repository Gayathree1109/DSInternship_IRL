if __name__ == '__main__':
    N = int(input())
    li = []
    for i in range(N):
        li.append(input().split())
    a =[]
    for i in range(N):
        if li[i][0] == 'insert':
            a.insert(int(li[i][1]), int(li[i][2]))
        elif li[i][0] == 'print':
            print(a)
        elif li[i][0] == 'remove':
            a.remove(int(li[i][1]))
        elif li[i][0] == 'append':
            a.append(int(li[i][1]))
        elif li[i][0] == 'sort':
            a.sort()
        elif li[i][0] == 'pop':
            a.pop()
        elif li[i][0] == 'reverse':
            a.reverse()
        
                
            