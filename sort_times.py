import time
import array
import random
import plotter


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
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = partition(arr, low, high)
            if pivot > low:
                stack.append((low, pivot - 1))
            if pivot < high:
                stack.append((pivot + 1, high))


def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i



def sort_function_timer(sort_function, an_array):
    start = time.perf_counter()
    sort_function(an_array)
    end = time.perf_counter()
    total_time = (end - start) * 1000
    return total_time

SIZES = [200, 500, 800, 1100, 1400, 1700, 2000]

def plot_sort_time_using_random_array(sort_function):
    print('timming:', sort_function.__name__)
    plotter.new_series()

    for size in SIZES:
        arr = [random.randint(1, 10000) for _ in range(size)]
        time_taken = sort_function_timer(sort_function, arr)
        plotter.add_data_point(time_taken)


def plot_sort_time_using_sorted_array(sort_function):
    print('Timing (Sorted Array):', sort_function.__name__)
    plotter.new_series()

    for size in SIZES:
        sorted_array = list(range(1, size + 1))
        time_taken = sort_function_timer(sort_function, sorted_array)
        plotter.add_data_point(time_taken)

def main():
    # Initialize the plotter with title and labels
    plotter.init("Sorting Algorithm Performance",
                 "Array Size", "Time (seconds)")

    # Call the plot_sort_time_using_random_array function for each sorting algorithm
    plot_sort_time_using_random_array(merge_sort)
    plot_sort_time_using_random_array(quickSort)
    plot_sort_time_using_random_array(naive_sort)

    # Add data for sorted arrays
    plot_sort_time_using_sorted_array(naive_sort)
    plot_sort_time_using_sorted_array(merge_sort)
    plot_sort_time_using_sorted_array(quickSort)

    # Plot the results
    plotter.plot()
    input()

if __name__ == "__main__":
    main()
