import random
import time

from algorithms import bubble_sort, selection_sort, insertion_sort

def generate_random_array(size):
    return random.choices(range(1_000_000), k=size) # genrating lists with random number  

sizes = [10000, 25000, 50000, 75000,100000]

for size in sizes:
    print(f"\n--- Testing Array Size: {size} ---")
    base_arr = generate_random_array(size)

    #  Bubble Sort
    arr_bubble = base_arr.copy()
    start = time.time()
    bubble_sort(arr_bubble)
    end = time.time()
    bubble_time = (end - start) * 1000
    print(f"Running time for Bubble Sort is {bubble_time:.2f} ms")

    #  Selection Sort
    arr_selection = base_arr.copy()
    start = time.time()
    selection_sort(arr_selection)
    end = time.time()
    selection_time = (end - start) * 1000
    print(f"Running time for Selection Sort is {selection_time:.2f} ms")

    #  Insertion Sort
    arr_insertion = base_arr.copy()
    start = time.time()
    insertion_sort(arr_insertion)
    end = time.time()
    insertion_time = (end - start) * 1000
    print(f"Running time for Insertion Sort is {insertion_time:.2f} ms")