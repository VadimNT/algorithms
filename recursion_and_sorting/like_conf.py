def lovely_conf(n, edu, k):
    def quicksort(data):
        if len(data) < 2:
            return

        left = []
        middle = []
        right = []

        pivot = data[0]

        for i in range(len(data)):
            if data[i] == pivot:
                middle.append(pivot)
            elif data[i] < pivot:
                left.append(data[i])
            else:
                right.append(data[i])

        quicksort(left)
        quicksort(right)

        i = 0
        for x in left + middle + right:
            data[i] = x
            i += 1
        return

    quicksort(edu)

    rate_edu = {}
    for item in edu:
        if item in rate_edu:
            rate_edu[item] += 1
        else:
            rate_edu[item] = 1
    result = sorted(rate_edu, key=rate_edu.get, reverse=True)

    for i in range(k):
        print(result[i], end=' ')


if __name__ == '__main__':
    count_edu = int(input())
    id_edu = [int(x) for x in input().split()]
    k_edu_out = int(input())
    lovely_conf(count_edu, id_edu, k_edu_out)
