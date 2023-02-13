def get_anagram_idx(data, n):
    result = {}
    for i in range(n):
        data[i] = ''.join(sorted(data[i]))
        if data[i] not in result:
            result[data[i]] = str(i)
        else:
            result[data[i]] += ' ' + str(i)

    for res in result.values():
        print(res)


if __name__ == '__main__':
    length = int(input())
    data_in = input().split()
    get_anagram_idx(data_in, length)
