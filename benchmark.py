import random
import time
import matplotlib.pyplot as plt
from algorithms import bubble_sort, selection_sort, insertion_sort


btime=[]
stime=[]
itime=[]

def generate_random_array(size):
    return random.choices(range(1_000_000), k=size) # genrating lists with random number  

sizes = [10000, 25000, 50000, 100000]

for size in sizes:
    print(f"\n--- Testing Array Size: {size} ---")
    base_arr = generate_random_array(size)

    #  Bubble Sort
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




plt.figure(figsize=(8, 5))
plt.plot(sizes, btime, label="Bubble sort", color="blue", marker="o")
plt.plot(sizes, stime, label="Selection sort", color="red", marker="o")
plt.plot(sizes, itime, label="Insertion sort", color="gold", marker="o")

plt.xlabel("Input size (N)")
plt.ylabel("Execution time (ms)")
plt.title("Sorting Algorithms Execution Time")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

# Save first, then display
plt.savefig("sorting_benchmark.png", dpi=300, bbox_inches="tight")
plt.show()