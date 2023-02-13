def foo(data):
    if data in (0, 1):
        return 1
    return foo(data - 1) + foo(data - 2)


if __name__ == '__main__':
    n = int(input())
    print(foo(n))
