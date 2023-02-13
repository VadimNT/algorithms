def combinations(data):
    telephone_keys = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    result = []

    def get_combinations(buttons_tel, comb, res):
        if not buttons_tel:
            res.append(comb)
            return
        for key in telephone_keys[buttons_tel[0]]:
            comb += key
            get_combinations(buttons_tel[1:], comb, res)
            comb = comb[:-1]

    get_combinations(data, '', result)

    for item in result:
        print(item, end=' ')


if __name__ == '__main__':
    in_data = input()
    combinations(in_data)
