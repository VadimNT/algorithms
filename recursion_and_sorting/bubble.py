def sort_bubble(data):
    flag = False
    for i in range(1, len(data)):
        tmp = data.copy()
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                flag = True
        if tmp != data:
            for item in data:
                print(item, end=' ')
            print()
    if not flag:
        for item in data:
            print(item, end=' ')
        print()


if __name__ == '__main__':
    n = input()
    array = list(map(int, input().split()))
    sort_bubble(array)
