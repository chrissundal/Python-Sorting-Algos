from main import draw_list

def bubble_sort(array,draw_info):
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED})
                yield True
    return array

def selection_sort(array, draw_info):
    for i in range(0, len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
                draw_list(draw_info, {j: draw_info.RED, min_index: draw_info.GREEN})
                yield True
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
            draw_list(draw_info, {i: draw_info.GREEN, min_index: draw_info.RED})
            yield True
    return array

def insertion_sort(array, draw_info):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        draw_list(draw_info, {i: draw_info.RED})
        yield True
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED})
            yield True
            j -= 1
        array[j + 1] = key
        draw_list(draw_info, {j + 1: draw_info.GREEN})
        yield True
    return array


def counting_sort(array, draw_info):
    max_val = max(array)
    min_val = min(array)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    for num in array:
        count[num - min_val] += 1

    sorted_index = 0
    for i in range(range_of_elements):
        while count[i] > 0:
            array[sorted_index] = i + min_val
            draw_list(draw_info, {sorted_index: draw_info.RED})
            yield True
            sorted_index += 1
            count[i] -= 1
    return array


def merge_sort(array, draw_info):
    if len(array) <= 1:
        return array

    temp_array = array.copy()
    yield from merge_sort_helper(array, temp_array, 0, len(array) - 1, draw_info)
    return array


def merge_sort_helper(array, temp_array, first, last, draw_info):
    if first < last:
        middle = (first + last) // 2
        yield from merge_sort_helper(temp_array, array, first, middle, draw_info)
        yield from merge_sort_helper(temp_array, array, middle + 1, last, draw_info)
        yield from merge_arrays(array, temp_array, first, middle, last, draw_info)


def merge_arrays(array, temp_array, first, middle, last, draw_info):
    i = first
    j = middle + 1
    k = first

    while i <= middle and j <= last:
        draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED})
        yield True

        if temp_array[i] <= temp_array[j]:
            array[k] = temp_array[i]
            i += 1
        else:
            array[k] = temp_array[j]
            j += 1
        k += 1

    while i <= middle:
        array[k] = temp_array[i]
        draw_list(draw_info, {k: draw_info.RED, i: draw_info.GREEN})
        yield True
        i += 1
        k += 1

    while j <= last:
        array[k] = temp_array[j]
        draw_list(draw_info, {k: draw_info.RED, j: draw_info.GREEN})
        yield True
        j += 1
        k += 1


# def merge_sort_2(array,draw_info):
#     if len(array) > 1:
#         mid = len(array) // 2
#         left_half = array[:mid]
#         right_half = array[mid:]
#         merge_sort_2(left_half)
#         merge_sort_2(right_half)
#
#         i = j = k = 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 array[k] = left_half[i]
#                 i += 1
#             else:
#                 array[k] = right_half[j]
#                 j += 1
#             k += 1
#
#         while i < len(left_half):
#             array[k] = left_half[i]
#             i += 1
#             k += 1
#
#         while j < len(right_half):
#             array[k] = right_half[j]
#             j += 1
#             k += 1

# def quick_sort(array,draw_info):
#     if len(array) <= 1:
#         return array
#     pivot = array[len(array) // 2]
#     left = [x for x in array if x < pivot]
#     middle = [x for x in array if x == pivot]
#     right = [x for x in array if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)

def quick_sort(array, draw_info):
    yield from quick_sort_helper(array, 0, len(array) - 1, draw_info)
    return array

def quick_sort_helper(array, low, high, draw_info):
    if low < high:
        pivot_idx = yield from partition(array, low, high, draw_info)
        yield from quick_sort_helper(array, low, pivot_idx - 1, draw_info)
        yield from quick_sort_helper(array, pivot_idx + 1, high, draw_info)
def partition(array, low, high, draw_info):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        draw_list(draw_info, {j: draw_info.RED, high: draw_info.GREEN})
        yield True

        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED})
            yield True

    array[i + 1], array[high] = array[high], array[i + 1]
    draw_list(draw_info, {i + 1: draw_info.GREEN, high: draw_info.RED})
    yield True

    return i + 1

def heap_sort(array, draw_info):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(array, n, i, draw_info)

    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        draw_list(draw_info, {0: draw_info.RED, i: draw_info.GREEN})
        yield True
        yield from heapify(array, i, 0, draw_info)

    return array

def heapify(array, n, i, draw_info):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        draw_list(draw_info, {i: draw_info.RED, largest: draw_info.GREEN})
        yield True
        yield from heapify(array, n, largest, draw_info)


def org_sort(array):
    return array.sort()
