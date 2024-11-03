def heap_sort(arr, max_swaps):
    n = len(arr)
    swap_count = [0]

    build_min_heap(arr, n, max_swaps, swap_count)
    if swap_count[0] >= max_swaps:
        return swap_count[0]

    for i in range(n - 1, 0, -1):
        if swap_count[0] >= max_swaps:
            break
        arr[0], arr[i] = arr[i], arr[0]
        swap_count[0] += 1
        if swap_count[0] >= max_swaps:
            break
        heapify(arr, 0, i, max_swaps, swap_count)

    return swap_count[0]

def build_min_heap(arr, n, max_swaps, swap_count):
    for i in range((n // 2) - 1, -1, -1):
        if swap_count[0] >= max_swaps:
            break
        heapify(arr, i, n, max_swaps, swap_count)

def heapify(arr, k, n, max_swaps, swap_count):
    left = 2 * k + 1
    right = 2 * k + 2
    smaller = k

    if left < n and arr[left] < arr[smaller]:
        smaller = left

    if right < n and arr[right] < arr[smaller]:
        smaller = right

    if smaller != k:
        arr[k], arr[smaller] = arr[smaller], arr[k]  # Swap
        swap_count[0] += 1
        if swap_count[0] >= max_swaps:
            return
        heapify(arr, smaller, n, max_swaps, swap_count)

n, k = map(int, input().split())
arr = list(map(int, input().split()))

swap_count = heap_sort(arr, k)

if swap_count < k:
    print(-1)
else:
    print(" ".join(map(str, arr)))