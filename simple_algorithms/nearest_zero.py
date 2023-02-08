def get_input_data():
    n = int(input())
    array = [int(item) for item in input().split()]
    return n, array


def output_result(result):
    return print(*result)


def nearest_zero():
    n, data = get_input_data()
    zero_index_right = zero_index_left = data.index(0)
    distance_to_zero_for_each = []
    digit = 0
    while digit < n:
        if data[digit] == 0:
            distance_to_zero_for_each.append(0)
            zero_index_left = digit
            try:
                zero_index_right = data.index(0, digit + 1, n + 1)
            except Exception:
                pass
            digit += 1
            continue
        if abs(digit - zero_index_left) <= abs(digit - zero_index_right):
            distance_to_zero_for_each.append(abs(digit - zero_index_left))
        else:
            distance_to_zero_for_each.append(abs(digit - zero_index_right))
        digit += 1
    output_result(distance_to_zero_for_each)


if __name__ == '__main__':
    nearest_zero()
