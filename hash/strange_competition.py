def is_strange_comparison(a_word, b_word):
    if len(a_word) == len(b_word):
        a_dict = {}
        b_dict = {}
        result = 'YES'

        for j in range(0, len(b_word)):
            a = a_word[j]
            b = b_word[j]
            if b_dict.get(a, None) is None:
                b_dict[a] = b
                a_dict[b] = a
            elif b_dict.get(a) != b or a_dict.get(b) != a:
                result = 'NO'
                break

        print(result)

    else:
        print('NO')


if __name__ == '__main__':
    str_one = input()
    str_two = input()
    is_strange_comparison(str_one, str_two)
