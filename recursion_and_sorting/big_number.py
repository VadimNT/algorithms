def compare(one_num, two_num):
    if len(one_num) == len(two_num):
        return int(one_num) < int(two_num)
    else:
        var1 = one_num + two_num
        var2 = two_num + one_num
        return var1 < var2


def get_max_number(n, data, comparator):
    result = ''
    for i in range(1, n):
        for j in range(n - 1):
            if comparator(data[j], data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]
    for item in data:
        result += str(item)
    print(result)


if __name__ == '__main__':
    size = int(input())
    array = list(map(str, input().split()))
    get_max_number(size, array, compare)
