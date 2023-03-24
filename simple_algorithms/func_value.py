def func(in_data):
    a, x, b, c = (value for value in in_data)
    return print(
        a * x ** 2 + b * x + c
    )


if __name__ == '__main__':
    in_list = [int(i) for i in input().split()]
    func(in_list)
