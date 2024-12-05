phrase = input()
x = phrase.find("+")
p = "+"
if x == -1:
    p = "*"
    x = phrase.find("*")
if x == -1:
    p = "-"
    x = phrase.find("-")
y = phrase.find("=")
a = int(phrase[0:x])
b = int(phrase[x+1:y])
c = int(phrase[y+1:len(phrase)])
if p == "+":
    if a+b == c:
        print("Yes")
    else:
        print(a+b)
elif p == "-":
    if a-b == c:
        print("Yes")
    else:
        print(a-b)
elif p == "*":
    if a*b == c:
        print("Yes")
    else:
        print(a*b)
