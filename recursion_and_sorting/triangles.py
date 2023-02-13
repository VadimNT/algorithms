def get_max_perimetr(n, len_segment):
    len_segment = sorted(len_segment, reverse=True)

    for i in range(len(len_segment) - 2):
        if len_segment[i] < len_segment[i + 1] + len_segment[i + 2]:
            print(len_segment[i] + len_segment[i + 1] + len_segment[i + 2])
            break


if __name__ == '__main__':
    size = int(input())
    data = [int(x) for x in input().split()]
    get_max_perimetr(size, data)
