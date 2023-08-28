import time
import numpy as np
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, M = arr[:mid], arr[mid:]
        merge_sort(L)
        merge_sort(M)
        arr[:] = sorted(L + M)

def quick_sort(arr):
    return arr if len(arr) <= 1 else quick_sort([x for x in arr if x < arr[len(arr) // 2]]) + [x for x in arr if x == arr[len(arr) // 2]] + quick_sort([x for x in arr if x > arr[len(arr) // 2]])

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = min(range(i, len(arr)), key=arr.__getitem__)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def read_input():
    n = int(input("Enter the number of TV Channels: "))
    print("Enter the number of viewers for each TV Channel")
    return [int(input(f"Enter the number of viewers for TV Channel {i+1}: ")) for i in range(n)]

def time_analysis(sorting_func, label_data):
    elements, times = [], []
    
    print("******************Running Time Analysis*******************")
    for i in range(1, 10):
        arr = np.random.randint(0, 1000 * i, 1000 * i)
        start = time.time()
        sorting_func(arr)
        end = time.time()
        print(len(arr), "Elements Sorted by", label_data, end - start)
        elements.append(len(arr))
        times.append(end - start)
    
    plt.xlabel('List Length')
    plt.ylabel('Time Complexity')
    plt.plot(elements, times, label=label_data)
    plt.grid()
    plt.legend()
    plt.show()

print("1. Merge sort 2. Quick Sort 3. Selection Sort")
choice = int(input("Enter the Choice: "))

if choice == 1:
    arr = read_input()
    merge_sort(arr)
    print('Sorted Array:', arr)
    time_analysis(merge_sort, "MergeSort")
elif choice == 2:
    arr = read_input()
    quick_sort(arr, 0, len(arr) - 1)
    print('Sorted Array:', arr)
    time_analysis(lambda arr: quick_sort(arr, 0, len(arr) - 1), "QuickSort")
elif choice == 3:
    arr = read_input()
    selection_sort(arr)
    print('Sorted Array:', arr)
    time_analysis(selection_sort, "SelectionSort")
else:
    print("Invalid choice")