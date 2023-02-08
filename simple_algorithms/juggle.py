def get_input_data():
    k = int(input()) * 2
    str_in = ''
    str_in = ''.join([str_in + input() for i in range(4)])
    return k, str_in


def output_result(result):
    print(result)


def sleight_of_hand():
    k, data = get_input_data()
    points = 0
    number_key = 0
    while number_key < 10:
        num_of_press_key = data.count(str(number_key))
        if num_of_press_key <= k and num_of_press_key != 0:
            points += 1
        number_key += 1
    output_result(points)


if __name__ == '__main__':
    sleight_of_hand()
