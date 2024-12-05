if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = list(arr)
    l.sort()
    i = len(l)-2
    while l[i] == l[i+1]:
        i -= 1
    print(l[i])
