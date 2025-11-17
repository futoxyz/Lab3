def partition(a: list[int], low: int, high: int) -> int:
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

def quick_sort_step(a: list[int], low: int, high: int):
    if low < high:
        i = partition(a, low, high) - 1
        quick_sort_step(a, low, i)
        quick_sort_step(a, i + 2, high)


def digit(n: int, exp: int, base: int) -> int:
    return (n // exp) % base


def digit_sort(a: list[int], digit_a: list[int]) -> list[int]:
    length = len(digit_a)
    sorted = False
    while not sorted:
        for i in range(length - 1):
            if digit_a[i+1] < digit_a[i]:
                a[i], a[i+1] = a[i+1], a[i]
                digit_a[i], digit_a[i + 1] = digit_a[i + 1], digit_a[i]
                break
            if i == length - 2:
                sorted = True
    return a


def insertion_sort(bucket: list[float]) -> list[float]:
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket
