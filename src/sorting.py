from src.sorting_extra import *

'''
Все функции принимают только список (целых чисел), возврат - отсортированный список.
'''

def bubble_sort(a: list[int]) -> list[int]:
    is_correct(a)
    n = len(a)
    sorted = False
    while not sorted:
        for i in range(n - 1):
            if a[i+1] < a[i]:
                a[i], a[i+1] = a[i+1], a[i]
                break
            if i == n - 2:
                sorted = True
    return a


def quick_sort(a: list[int]) -> list[int]:
    is_correct(a)
    quick_sort_step(a, 0, len(a) - 1)
    return a


def counting_sort(a: list[int]) -> list[int]:
    is_correct(a)
    n = len(a)
    largest = max(a)
    count_a = [0] * (largest + 1)
    ans = [0]*n
    for i in a:
        count_a[i] += 1
    for j in range(1, largest + 1):
        count_a[j] += count_a[j - 1]

    for i in range(n - 1, -1, -1):
        x = a[i]
        ans[count_a[x] - 1] = x
        count_a[x] -= 1

    return ans


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    '''
    :param base: Необязательный параметр - основание разрядов для сортировки.
    '''
    is_correct(a)
    largest = max(a)
    exp = 1
    while largest // exp > 0:
        digit_a = []
        for k in range(len(a)):
            el = a[k]
            digit_a.append(digit(el, exp, base))
        a = counting_digit_sort(digit_a, a)
        exp *= base
    return a


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    '''
    :param a: Список чисел с плавающей точкой.
    :param buckets: Необязательный параметр - количество ведер для сортировки.
    '''
    is_correct_float(a)
    if not buckets:
        buckets = len(a)
    minimum = min(a)
    largest = max(a)
    bucket_range = (largest - minimum)
    arr = [[] for _ in range(buckets)]
    for num in a:
        index = int((num - minimum) / bucket_range * buckets)
        if index == buckets:
            index -= 1
        arr[index].append(num)
    for i in range(buckets):
        if arr[i]:
            arr[i] = quick_sort_bucket(arr[i])
    ans = []
    for bucket in arr:
        ans.extend(bucket)

    return ans

def heap_sort(a: list[int]) -> list[int]:
    is_correct(a)
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)

    return a
