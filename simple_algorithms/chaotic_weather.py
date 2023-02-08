def main():
    n = int(input())
    line = []
    line.append(-274)
    line = list(map(int, input().split()))
    line.append(-274)
    i = result = 0
    while i <= n:
        if line[i - 1] < line[i] > line[i + 1]:
            result += 1
        i += 1
    return print(result)


if __name__ == '__main__':
    main()
