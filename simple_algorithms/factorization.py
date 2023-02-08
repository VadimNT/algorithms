def factor():
    in_data = int(input())
    result = []
    d = 2
    while d * d <= in_data:
        if in_data % d == 0:
            result.append(d)
            in_data //= d
        else:
            d += 1
    if in_data > 1:
        result.append(in_data)
    return print(*result)


if __name__ == '__main__':
    factor()
