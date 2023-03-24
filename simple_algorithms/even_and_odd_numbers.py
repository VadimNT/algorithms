def func(in_data: list) -> str:
    even = odd = False
    for value in in_data:
        if not value % 2:
            even = True
        else:
            odd = True
        if even == odd:
            return 'FAIL'
    return 'WIN'


if __name__ == '__main__':
    in_list = [int(i) for i in input().split()]
    print(func(in_list))
