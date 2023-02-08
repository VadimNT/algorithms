def main():
    n = int(input())
    max_value = 10000
    degree = 0
    while 4 ** degree < max_value:
        degree += 1

    for i in range(degree):
        if 4 ** i == n:
            return True
    return False


if __name__ == '__main__':
    print(main())
