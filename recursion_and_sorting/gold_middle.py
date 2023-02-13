def get_median(size_l, size_r, left, right):
    if left[-1] <= right[0]:
        result = left + right
    elif left[0] >= right[-1]:
        result = right + left
    else:
        result = [0] * (size_l + size_r)

        l, r, k = 0, 0, 0

        while l < size_l and r < size_r:
            if left[l] <= right[r]:
                result[k] = left[l]
                l += 1
            else:
                result[k] = right[r]
                r += 1
            k += 1
        if l == size_l:
            result += left[l:]
        else:
            result += right[r:]

    mid = int((size_l + size_r) / 2)
    if not (size_l + size_r) % 2:
        return (result[mid - 1] + result[mid]) / 2
    return result[mid]


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    left_land = [int(x) for x in input().split()]
    right_land = [int(x) for x in input().split()]
    print(get_median(n, m, left_land, right_land))
