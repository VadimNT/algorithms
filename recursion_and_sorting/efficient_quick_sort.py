# 80094054
class User:
    __slots__ = ['name', 'num_task', 'time_penalty']

    def __init__(self, name, num_task, time_penalty):
        self.name = name
        self.num_task = int(num_task)
        self.time_penalty = int(time_penalty)

    def userdata(self):
        return -self.num_task, self.time_penalty, self.name

    def __gt__(self, other):
        return self.userdata() > other.userdata()

    def __lt__(self, other):
        return other > self

    def __str__(self):
        return self.name


def quicksort(users_data: list) -> None:
    def __quicksort_wh_start_end(data: list, start: int, end: int) -> None:
        if start >= end:
            return None

        left, right = start, end
        middle = (left + right) // 2
        pivot = data[middle]

        while left <= right:
            while data[left] < pivot:
                left += 1
            while data[right] > pivot:
                right -= 1
            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1
        __quicksort_wh_start_end(data, start, right)
        __quicksort_wh_start_end(data, left, end)

    __quicksort_wh_start_end(users_data, 0, n - 1)


if __name__ == '__main__':
    n = int(input())
    users = [
        User(*input().split()) for _ in range(n)
    ]
    quicksort(users)
    print(*users, sep='\n')
