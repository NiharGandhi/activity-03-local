import time
from sorts import quickSort, naive_sort, merge_sort, quick_insertion_sort
import random
import plotter

def sort_function_timer(sort_function, an_array):
    start = time.perf_counter()
    sort_function(an_array)
    end = time.perf_counter()
    total_time = (end - start) / 60
    return total_time

SIZES = [200, 500, 800, 1100, 1400, 1700, 2000]

def plot_sort_time_using_random_array(sort_function):
    print('timming:', sort_function.__name__)
    plotter.new_series() 

    for element in SIZES:
        arr = [random.randint(1, 10000) for _ in range(element)]
        time_taken = sort_function_timer(sort_function, arr)
        plotter.add_data_point(time_taken)


def plot_sort_time_using_sorted_array(sort_function):
    print('Timing (Sorted Array):', sort_function.__name__)
    plotter.new_series()

    for element in SIZES:
        sorted_array = list(range(1, element + 1))
        time_taken = sort_function_timer(sort_function, sorted_array)
        plotter.add_data_point(time_taken)

def main():
    # Initialize the plotter with title and labels
    plotter.init("Sorting Algorithm Performance",
                 "Array Sizes", "Time Taken ")

    # Call the plot_sort_time_using_random_array function for each sorting algorithm
    plot_sort_time_using_random_array(merge_sort)
    plot_sort_time_using_random_array(quickSort)
    plot_sort_time_using_random_array(naive_sort)

    # Add data for sorted arrays
    # plot_sort_time_using_sorted_array(naive_sort)
    # plot_sort_time_using_sorted_array(merge_sort)
    # plot_sort_time_using_sorted_array(quickSort)

    # Hybrid Sort
    plot_sort_time_using_random_array(quick_insertion_sort)
    plot_sort_time_using_sorted_array(quick_insertion_sort)

    # Plot the results
    plotter.plot()
    input()

if __name__ == "__main__":
    main()
