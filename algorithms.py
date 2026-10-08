def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # or just use temp
                swapped = True
        if not swapped: # to check that its already sorted or no
            break
    return arr
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

def selection_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        k=i
        for j in range(i+1,n):
            if arr[j] < arr[k]:
                k=j

        arr[i],arr[k] = arr[k],arr[i]