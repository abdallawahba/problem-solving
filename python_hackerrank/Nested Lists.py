if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        nl = []
        name = input()
        score = float(input())
        nl.append(score)
        nl.append(name)
        l.append(nl)
    l.sort()
    fnd = l[1][0]
    for i in range(1,len(l)):
        if l[i-1][0] == l[i][0]:
            fnd = l[i+1][0]
        else:
            break
    for i in range(len(l)):
        if fnd == l[i][0]:
            print(l[i][1])
            