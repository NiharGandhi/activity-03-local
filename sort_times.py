import random
import plotter
import time
from sorts import quickSort
from sorts_2 import insertion_sort, merge_sort, quicksort, quick_insertion_sort

def sort_funtion_timer(sort_funtion, an_array):
    start = time.perf_counter()
    sort_funtion(an_array)
    end = time.perf_counter()
    exec_time = round((end - start), 5)
    return exec_time


SIZES = [200, 500, 800, 1100, 1400, 1700, 2000]

def range_array():
    main_array = []
    for size in SIZES:
        arr = []
        i = 0
        while i < size:
            arr.append(random.randint(1, 1000))
            i += 1
        main_array.append(arr)
    return main_array

full_array = range_array()

def plot_sort_time_using_random_arrays(sort_function):
    print('timing:', sort_function.__name__)
    plotter.new_series()
    for array in full_array:
        time_taken = sort_funtion_timer(sort_function, array)
        plotter.add_data_point(time_taken)

def plot_sort_time_using_sorted_z(sort_function):
    print('timing (for Sorted Array):', sort_function.__name__)
    plotter.new_series()
    for array in full_array:
        array.sort()
        time_taken = sort_funtion_timer(sort_function, array)
        plotter.add_data_point(time_taken)

sort_functions = [insertion_sort, merge_sort, quicksort]

def main():
    plotter.init('Time Complexity', 'Array Size', 'Time Taken')
    # print('RANDOM ARRAYS')
    # for sort in sort_functions:
    #     plot_sort_time_using_random_arrays(sort)
    
    print('SORTED ARRAYES')
    for sort in sort_functions:
        plot_sort_time_using_sorted_z(sort)

    # print('QUICK INSERTION SORT')
    # plot_sort_time_using_random_arrays(quick_insertion_sort)
    # plot_sort_time_using_sorted_z(quick_insertion_sort)

    plotter.plot()
    input('Hit Enter: ')

if __name__ == '__main__':
    main()