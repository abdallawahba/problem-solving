cube = lambda x: pow(x, 3)


def fibonacci(n):
    fib = []
    for i in range(n):
        if i == 0 or i == 1:
            fib.append(i)
        else:
            fib.append(fib[i-1]+fib[i-2])
    return fib


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
