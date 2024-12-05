def minion_game(t):
    lv = ['A', 'I', 'O', 'E', 'U']
    ls = 0
    lk = 0
    for i in range(len(t)):
        if t[i] in lv:
            lk += len(t)-i
        else:
            ls += len(t)-i
    if lk>ls:
        print("Kevin",end=' ')
        print(lk)
    elif lk == ls:
        print("Draw")
    else:
        print("Stuart", end=' ')
        print(ls)


s = input()
minion_game(s)