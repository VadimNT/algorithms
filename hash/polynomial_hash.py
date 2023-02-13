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


if __name__ == '__main__':
    base = int(input())
    modul = int(input())
    in_data = input()
    print(polynomial_hash(in_data, base, modul))
