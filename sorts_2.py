def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while arr[j - 1] > key and j > 0:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = key
    

def merge_sort(data):
    arr = data.copy()
    if len(arr) <= 1:
        return arr

    # Split the array into even and odd indexed subarrays
    left = arr[::2]
    right = arr[1::2]

    # Recursively sort the subarrays
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted subarrays
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    # Compare elements in the subarrays and then adding the smaller element first to the new array.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements from the subarrays to the new array.
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

def quicksort(data):
    arr = data.copy()

    if len(arr) <= 1:
     return arr

    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


def quick_insertion_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    # Check if the array is nearly sorted
    if abs(arr[0] - arr[-1]) < 900:
        return arr

    # Recursively sort the subarrays if the array is not nearly sorted
    left_sorted = quick_insertion_sort(left)
    right_sorted = quick_insertion_sort(right)

    return left_sorted + [pivot] + right_sorted
