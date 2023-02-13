def foo(data):
    ab = [1, 1]
    fib = None
    d = (10 ** data[1])
    if data[0] < 2:
        fib = 1
    else:
        data[0] -= 1
        for i in range(data[0]):
            s = (ab[0] + ab[1]) % d
            ab[0] = ab[1]
            ab[1] = s
            fib = ab[1]
    return fib


if __name__ == '__main__':
    data = list(map(int, input().split()))
    print(foo(data))
