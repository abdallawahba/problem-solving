def merge_the_tools(t, k):
    l = int(len(t)/k)  # num of sub strings = l AND num of characters <= k
    b = 0
    for _ in range(l):
        letters = []
        for i in range(k):
            if not (t[b] in letters):
                letters.append(t[b])
            b += 1
        for j in range(len(letters)):
            print(letters[j], end='')
        print("")


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)