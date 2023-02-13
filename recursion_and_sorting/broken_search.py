# 80081404
from typing import List


def broken_search(nums: List[int], target: int) -> int:
    def __binary_search(left: int, right: int) -> int:
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1

    def __find_pivot(data_in: List[int]) -> int:
        start = 0
        end = len(data_in) - 1
        while start <= end:
            mid = (start + end) // 2
            if data_in[mid] >= data_in[end]:
                start = mid + 1
            else:
                end = mid
        return end if end else len(data_in) - 1

    pivot = __find_pivot(nums)

    if nums[pivot] == target:
        return pivot
    if nums[0] == target:
        return 0
    if nums[0] < target:
        return __binary_search(0, pivot - 1)
    return __binary_search(pivot + 1, len(nums) - 1)
