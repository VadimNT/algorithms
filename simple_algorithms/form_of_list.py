def get_list(x, k):
    return print(' '.join(list(map(str, list(str(x + k))))))


if __name__ == '__main__':
    n = int(input())
    in_x = int(input().replace(' ', ''))
    in_k = int(input())
    get_list(in_x, in_k)
