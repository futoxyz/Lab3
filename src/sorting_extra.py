def partition(a: list[int], low: int, high: int) -> int:
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

def quick_sort_step(a: list[int], low: int, high: int) -> None:
    if low < high:
        i = partition(a, low, high) - 1
        quick_sort_step(a, low, i)
        quick_sort_step(a, i + 2, high)


def digit(n: int, exp: int, base: int) -> int:
    if n>=0:
        return (n // exp) % base
    return - ((abs(n)// exp) % base)


def counting_digit_sort(digit_a: list[int], a: list[int]) -> list[int]:
    n = len(digit_a)
    largest = max(digit_a)
    count_a = [0] * (largest + 1)
    for i in digit_a:
        count_a[i] += 1
    for j in range(1, largest + 1):
        count_a[j] += count_a[j - 1]
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        x = digit_a[i]
        ans[count_a[x] - 1] = a[i]
        count_a[x] -= 1
    return ans


def insertion_sort(bucket: list[float]) -> list[float]:
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket


def heapify(a: list[int], length: int, large: int) -> None:
    i = large
    left = 2*large + 1
    right = 2*large + 2
    if left < length and a[left] > a[large]:
        large = left
    if right < length and a[right] > a[large]:
        large = right
    if i != large:
        a[i], a[large] = a[large], a[i]

    heapify(a, length, large)
