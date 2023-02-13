def find_two_day_buy_velocity(data, price, left, right):
    if right <= left != 0:
        return -1

    middle = (left + right) // 2
    if data[middle] >= price and (data[middle - 1] < price or middle == 0):
        return middle + 1
    elif price <= data[middle]:
        return find_two_day_buy_velocity(data, price, left, middle)
    else:
        return find_two_day_buy_velocity(data, price, middle + 1, right)


if __name__ == '__main__':
    days = int(input())
    money = list(map(int, input().split()))
    prc = int(input())

    print(find_two_day_buy_velocity(money, prc, 0, days), end=' ')
    print(find_two_day_buy_velocity(money, prc * 2, 0, days))
