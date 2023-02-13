def diff_trash_idx(n, data, k):
    result = []
    result.append(abs(data[0] - data[1]))
    for i in range(n - 1):
        for j in range(i + 1, n):
            result.append(abs(data[i] - data[j]))
            result = sorted(result, reverse=True)
            result.pop()
            if k <= 1:
                break
        if k <= 1:
            break
    print(result[0])


if __name__ == '__main__':
    size = int(input())
    trash_idx = [int(x) for x in input().split()]
    out_idx = int(input())
    diff_trash_idx(size, trash_idx, out_idx)
