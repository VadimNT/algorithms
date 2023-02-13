def polynomial_hash(s, a, m):
    if s == '':
        return 0
    if len(s) < 2:
        return ord(s) % m
    h = ord(s[-1])
    length = a
    for ch in s[-2::-1]:
        h += ord(ch) * length
        length = (length * a) % m
    return h % m


def get_coterie(data):
    coterie = {}
    a = 123
    m = 1000000007
    h = 0
    for item in data:
        h = polynomial_hash(item, a, m)
        if h not in coterie:
            coterie[h] = item
            print(item)


if __name__ == '__main__':
    count = int(input())
    data_in = [None] * count
    for i in range(count):
        data_in[i] = input()
    get_coterie(data_in)
