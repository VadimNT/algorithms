def get_flowerbed(n, data):
    result = []

    idx = 0
    big_start, big_end = data[idx]
    idx += 1

    while idx < n:
        if big_start <= flower_nums[idx][0] <= big_end:
            _, cur_end = flower_nums[idx]
            if cur_end > big_end:
                big_end = cur_end
        else:
            result.append([big_start, big_end])
            big_start, big_end = flower_nums[idx]
        idx += 1
    result.append([big_start, big_end])

    for res in result:
        print(*res)


if __name__ == '__main__':
    line = int(input())
    flower_nums = [0] * line
    for i in range(line):
        start, end = map(int, input().split())
        flower_nums[i] = [start, end]
    flower_nums.sort()
    get_flowerbed(line, flower_nums)
