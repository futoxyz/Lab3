from src.sorting_extra import *


def bubble_sort(a: list[int]) -> list[int]:
    length = len(a)
    sorted = False
    while not sorted:
        for i in range(length - 1):
            if a[i+1] < a[i]:
                a[i], a[i+1] = a[i+1], a[i]
                break
            if i == length - 2:
                sorted = True
    return a


def quick_sort(a: list[int]) -> list[int]:
    quick_sort_step(a, 0, len(a) - 1)
    return a


def counting_sort(a: list[int]) -> list[int]:
    n = len(a)
    largest = max(a)
    count_a = [0] * (largest + 1)
    for i in a:
        count_a[i] += 1
    for j in range(1, largest + 1):
        count_a[j] += count_a[j - 1]
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        x = a[i]
        ans[count_a[x] - 1] = x
        count_a[x] -= 1
    return ans


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    largest = max(a)
    exp = 1
    while largest // exp > 0:
        digit_a = []
        for k in range(len(a)):
            el = a[k]
            digit_a.append(digit(el, exp, base))
        a = digit_sort(a, digit_a)
        exp *= base
    return a


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    if buckets is None:
        buckets = len(a)
    min_val = min(a)
    max_val = max(a)
    bucket_range = (max_val - min_val) / buckets
    arr = [[] for _ in range(buckets)]
    for num in a:
        index = int((num - min_val) / bucket_range)
        if index == buckets:
            index -= 1
        arr[index].append(num)
    for i in range(buckets):
        arr[i] = insertion_sort(arr[i])
    result = []
    for bucket in arr:
        result.extend(bucket)

    return result
