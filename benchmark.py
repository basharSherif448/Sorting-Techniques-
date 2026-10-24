import random
import time
import matplotlib.pyplot as plt
from algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, heap_sort, quick_sort


btime = []
stime = []
itime = []
mtime = []
htime = []
qtime = []

def generate_random_array(size):
    return random.choices(range(1_000_000), k=size) # generating lists with random numbers  

sizes = [10000, 20000, 25000, 50000]

for size in sizes:
    print(f"\n--- Testing Array Size: {size} ---")
    base_arr = generate_random_array(size)

    # 1. Bubble Sort
    arr_bubble = base_arr.copy()
    start = time.time()
    bubble_sort(arr_bubble)
    end = time.time()
    bubble_time = (end - start) * 1000
    btime.append(bubble_time)
    print(f"Running time for Bubble Sort is {bubble_time:.2f} ms")

    # 2. Selection Sort
    arr_selection = base_arr.copy()
    start = time.time()
    selection_sort(arr_selection)
    end = time.time()
    selection_time = (end - start) * 1000
    stime.append(selection_time)
    print(f"Running time for Selection Sort is {selection_time:.2f} ms")

    # 3. Insertion Sort
    arr_insertion = base_arr.copy()
    start = time.time()
    insertion_sort(arr_insertion)
    end = time.time()
    insertion_time = (end - start) * 1000
    itime.append(insertion_time)
    print(f"Running time for Insertion Sort is {insertion_time:.2f} ms")

    # 4. Merge Sort
    arr_merge = base_arr.copy()
    start = time.time()
    merge_sort(arr_merge)
    end = time.time()
    merge_time = (end - start) * 1000
    mtime.append(merge_time)
    print(f"Running time for Merge Sort is {merge_time:.2f} ms")

    # 5. Heap Sort
    arr_heap = base_arr.copy()
    start = time.time()
    heap_sort(arr_heap)
    end = time.time()
    heap_time = (end - start) * 1000
    htime.append(heap_time)
    print(f"Running time for Heap Sort is {heap_time:.2f} ms")

    # 6. Quick Sort (takes low and high indices)
    arr_quick = base_arr.copy()
    start = time.time()
    quick_sort(arr_quick, 0, len(arr_quick) - 1)
    end = time.time()
    quick_time = (end - start) * 1000
    qtime.append(quick_time)
    print(f"Running time for Quick Sort is {quick_time:.2f} ms")


plt.figure(figsize=(8, 5))
plt.plot(sizes, btime, label="Bubble sort", color="blue", marker="o")
plt.plot(sizes, stime, label="Selection sort", color="red", marker="o")
plt.plot(sizes, itime, label="Insertion sort", color="gold", marker="o")
plt.plot(sizes, mtime, label="Merge sort", color="green", marker="o")
plt.plot(sizes, htime, label="Heap sort", color="purple", marker="o")
plt.plot(sizes, qtime, label="Quick sort", color="orange", marker="o")

plt.xlabel("Input size (N)")
plt.ylabel("Execution time (ms)")
plt.title("Sorting Algorithms Execution Time")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

# Save first, then display
plt.savefig("sorting_benchmark.png", dpi=300, bbox_inches="tight")
plt.show()