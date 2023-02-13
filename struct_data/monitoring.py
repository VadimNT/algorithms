def monitoring(data, n, m):
    for i in range(m):
        for j in range(n):
            print(data[j][i], end=' ')
        print('')


if __name__ == '__main__':
    n = int(input())
    m = int(input())

    in_data = []
    for i in range(n):
        in_data.append(input().split())

    monitoring(in_data, n, m)
