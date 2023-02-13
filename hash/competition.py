def get_result_competition(data, n):
    hash_table = {}
    total = 0
    max_len = 0

    for i in range(n):
        total += int(data[i])
        if total == 0:
            max_len = i + 1
        elif hash_table.get(total):
            max_len = max(max_len, i - hash_table[total])
        else:
            hash_table[total] = i

    return print(max_len)


if __name__ == '__main__':
    length = int(input())
    data_in = input()
    data_in = data_in.replace('0', '-1').split()
    get_result_competition(data_in, length)
