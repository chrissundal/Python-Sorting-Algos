import random
import time

unsorted = [random.randint(0, 10000) for i in range(10000)]

def bubble_sort(array):
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def selection_sort(array):
    for i in range(0,len(array) -1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    for num in arr:
        count[num - min_val] += 1

    sorted_index = 0
    for i in range(range_of_elements):
        while count[i] > 0:
            arr[sorted_index] = i + min_val
            sorted_index += 1
            count[i] -= 1
    return arr

def merge_sort(array):
    if len(array) <= 1:
        return array

    temp_array = array.copy()
    merge_sort2(array, temp_array, 0, len(array) - 1)

def merge_sort2(array, temp_array, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort2(temp_array, array, first, middle)
        merge_sort2(temp_array, array, middle + 1, last)
        merge(array, temp_array, first, middle, last)

def merge(array, temp_array, first, middle, last):
    i = first
    j = middle + 1
    k = first

    while i <= middle and j <= last:
        if temp_array[i] <= temp_array[j]:
            array[k] = temp_array[i]
            i += 1
        else:
            array[k] = temp_array[j]
            j += 1
        k += 1

    while i <= middle:
        array[k] = temp_array[i]
        i += 1
        k += 1

    while j <= last:
        array[k] = temp_array[j]
        j += 1
        k += 1

def merge_sort_2(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        merge_sort_2(left_half)
        merge_sort_2(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def heap_sort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)

def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def org_sort(array):
    return array.sort()

print(f"Unsorted: {unsorted} \n") if len(unsorted) <= 10000 else None

bubble_sorted = unsorted.copy()
start_time = time.time()
bubble_sorted = bubble_sort(bubble_sorted)
end_time = time.time()
bubble_sort_time = end_time - start_time
print(bubble_sorted) if len(unsorted) <= 10000 else None
print(f"Numbers: {len(bubble_sorted)} Bubble Sort Time: {bubble_sort_time:.6f} seconds \n")

selection_sorted = unsorted.copy()
start_time = time.time()
selection_sort(selection_sorted)
end_time = time.time()
selection_sort_time = end_time - start_time
print(selection_sorted) if len(unsorted) <= 10000 else None
print(f"Numbers: {len(selection_sorted)} Selection Sort Time: {selection_sort_time:.6f} seconds \n")

insertion_sorted = unsorted.copy()
start_time = time.time()
insertion_sort(insertion_sorted)
end_time = time.time()
insertion_sort_time = end_time - start_time
print(insertion_sorted) if len(unsorted) <= 10000 else None
print(f"Numbers: {len(insertion_sorted)} Insertion Sort Time: {insertion_sort_time:.6f} seconds \n")

org_sorted = unsorted.copy()
start_time = time.time()
org_sort(org_sorted)
end_time = time.time()
org_sort_time = end_time - start_time
print(org_sorted) if len(unsorted) <= 10000 else None
print(f"Numbers: {len(org_sorted)} Original Sort Time: {org_sort_time:.6f} seconds \n")

counting_sorted = unsorted.copy()
start_time = time.time()
counting_sorted = counting_sort(counting_sorted)
end_time = time.time()
counting_sort_time = end_time - start_time
print(counting_sorted) if len(unsorted) <= 10000 else None
print(f"Numbers: {len(counting_sorted)} Counting Sort Time: {counting_sort_time:.6f} seconds \n")

merge_sorted = unsorted.copy()
start_time = time.time()
merge_sort(merge_sorted)
end_time = time.time()
merge_sort_time = end_time - start_time
print(merge_sorted) if len(unsorted) <= 10000 else None
print(f"Numbers: {len(merge_sorted)} Merge Sort Time: {merge_sort_time:.6f} seconds \n")

merge_sorted_2 = unsorted.copy()
start_time = time.time()
merge_sort_2(merge_sorted_2)
end_time = time.time()
merge_sort_time_2 = end_time - start_time
print(merge_sorted) if len(unsorted) <= 10000 else None
print(f"Numbers: {len(merge_sorted_2)} Merge Sort 2 Time: {merge_sort_time_2:.6f} seconds \n")

quick_sorted = unsorted.copy()
start_time = time.time()
quick_sorted = quick_sort(quick_sorted)
end_time = time.time()
quick_sort_time = end_time - start_time
print(quick_sorted) if len(unsorted) <= 10000 else None
print(f"Numbers: {len(quick_sorted)} Quick Sort Time: {quick_sort_time:.6f} seconds \n")

heap_sorted = unsorted.copy()
start_time = time.time()
heap_sort(heap_sorted)
end_time = time.time()
heap_sort_time = end_time - start_time
print(heap_sorted) if len(unsorted) <= 10000 else None
print(f"Numbers: {len(heap_sorted)} Heap Sort Time: {heap_sort_time:.6f} seconds \n")