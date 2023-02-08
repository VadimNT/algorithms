arr = list(map(int, input().split()))


def func(array):
    flag_2 = i = 0
    while i < 3:
        if array[i] % 2:
            flag_2 += 1
        i += 1
    print('WIN') if flag_2 == 3 or flag_2 == 0 else print('FAIL')


func(arr)
