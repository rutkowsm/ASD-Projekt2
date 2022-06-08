def heapifyNd(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i].freq < arr[l].freq:
        largest = l

    if r < n and arr[largest].freq < arr[r].freq:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # <- SWAP ELEMENTS

        heapifyNd(arr, n, largest)


def heapSortNd(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapifyNd(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapifyNd(arr, i, 0)

    return arr
