import sys


def main():
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    x = int(input())
    y = int(input())
    result = []
    try:
        if x - 1 > -1:
            result.append(matrix[x - 1][y])
    except IndexError:
        pass
    try:
        result.append(matrix[x + 1][y])
    except IndexError:
        pass
    try:
        if y - 1 > -1:
            result.append(matrix[x][y - 1])
    except IndexError:
        pass
    try:
        result.append(matrix[x][y + 1])
    except IndexError:
        pass
    result.sort()
    print(" ".join(list(map(str, result))))


if __name__ == '__main__':
    main()
