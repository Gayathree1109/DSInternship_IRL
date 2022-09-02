
if __name__ == '__main__':
    a = []
    b = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a+= [[name,score]]
        b += [score]
    c= sorted(list(set(b)))[1]
    
    for i,j in sorted(a):
        if j == c:
            print(i)