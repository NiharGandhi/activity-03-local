"""
First we are import log from ma
"""
from math import log2

def naive_sort(data):
    for i in range(1, len(data)):
        j = i
        while data[j-1] > data[j] and j > 0:
            data[j-1], data[j] = data[j], data[j-1]
            j = j-1

    return data


def merge_sort(arr):
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


def quickSort(arr):
    if not arr:
        return []

    pivot = arr[0]
    less, same, more = partition_quick(pivot, arr)

    if len(less) > 0:
        less_lst = quickSort(less)
    else:
        less_lst = []

    same_lst = same
    more_lst = quickSort(more)

    return less_lst + same_lst + more_lst


def partition_quick(pivot, arr):
    less = []
    same = []
    more = []
    for i in range(0, len(arr)):
        if len(arr) == 0:
            break
        elif arr[i] < pivot:
            less.append(arr[i])
        elif arr[i] > pivot:
            more.append(arr[i])
        else:
            same.append(arr[i])
    return less, same, more


def quick_insertion_sort(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        start, end = stack.pop()

        if start < end:
            p = partition(arr, start, end)
            stack.append((start, p - 1))
            stack.append((p + 1, end))


def partition(arr, start, end):
    pivot = arr[end]
    idx = start - 1

    for idx_2 in range(start, end):
        if arr[idx_2] <= pivot:
            idx += 1
            arr[idx], arr[idx_2] = arr[idx_2], arr[idx]

    arr[idx + 1], arr[end] = arr[end], arr[idx + 1]
    return idx + 1
