def is1(s):
    for i in range(len(s)):
        if s[i].isalnum():
            return True
    return False


def is2(s):
    for i in range(len(s)):
        if s[i].isalpha():
            return True
    return False


def is3(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return True
    return False


def is4(s):
    for i in range(len(s)):
        if s[i].islower():
            return True
    return False


def is5(s):
    for i in range(len(s)):
        if s[i].isupper():
            return True
    return False


if __name__ == '__main__':
    s = input()
    print(is1(s))
    print(is2(s))
    print(is3(s))
    print(is4(s))
    print(is5(s))
