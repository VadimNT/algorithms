def main():
    num = int(input())
    if num == 0:
        return print(0)
    degree = 13
    result = ''
    value = 0
    while degree > -1:
        if 2 ** degree <= num:
            value += 2 ** degree
            if value <= num:
                result += '1'
            else:
                result += '0'
                value -= 2 ** degree
        degree -= 1
    return print(result)


if __name__ == '__main__':
    main()
