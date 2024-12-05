import re
n = int(input())
l = []
for i in range(n):
    stringx = input()
    if re.fullmatch(r'insert\s\d\s\d{1,}',stringx) is not None:
        x, y, z =stringx.split()
        l.insert(int(y),int(z))
    elif re.fullmatch(r'print',stringx) is not None:
        print(l)
    elif re.fullmatch(r'remove\s\d{1,}',stringx) is not None:
        x, y = stringx.split()
        l.remove(int(y))
    elif re.fullmatch(r'append\s\d{1,}',stringx) is not None:
        x, y = stringx.split()
        l.append(int(y))
    elif re.fullmatch(r'sort',stringx) is not None:
        l.sort()
    elif re.fullmatch(r'pop',stringx) is not None:
        l.pop()
    elif re.fullmatch(r'reverse',stringx) is not None:
        l.reverse()
