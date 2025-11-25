

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1

        while arr[j + 1] < arr[j] and j >= 0:
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = tmp
            j -= 1

    return arr


arr = [2, 3, 4, 1, 6]
print(insertion_sort(arr))