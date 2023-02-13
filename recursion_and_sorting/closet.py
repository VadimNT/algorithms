def wardrobe(data):
    closet = {
        '0': 0,
        '1': 0,
        '2': 0
    }
    for item in data:
        closet[item] += 1
    print('0 ' * closet['0'] + '1 ' * closet['1'] + '2 ' * closet['2'])


if __name__ == '__main__':
    n = int(input())
    in_data = [x for x in input().split()]
    wardrobe(in_data)
