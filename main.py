import csv
import time

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n-1):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return comparisons, swaps

def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j+1] = arr[j]
            swaps += 1
            j -= 1
        arr[j+1] = key
        swaps += 1
    return comparisons, swaps

def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1
    return comparisons, swaps

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    comparisons = 0
    swaps = 0
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                comparisons += 1
                arr[j] = arr[j-gap]
                swaps += 1
                j -= gap
            arr[j] = temp
            swaps += 1
        gap //= 2
    return comparisons, swaps


# Чтение CSV файла
with open('lab_1_read.csv', 'r') as file:
    reader = csv.reader(file)
    array = list(reader)[0]
# Сортировка пузырьком
array_bubble = array.copy()
start_time_bubble = time.perf_counter_ns()
bubble_comparisons, bubble_swaps = bubble_sort(array_bubble)
end_time_bubble = time.perf_counter_ns()
duration_bubble = end_time_bubble - start_time_bubble
# Сортировка вставкой
array_insertion = array.copy()
start_time_insertion = time.perf_counter_ns()
insertion_comparisons, insertion_swaps = insertion_sort(array_insertion)
end_time_insertion = time.perf_counter_ns()
duration_insertion = end_time_insertion - start_time_insertion
# Сортировка выбором
array_selection = array.copy()
start_time_selection = time.perf_counter_ns()
selection_comparisons, selection_swaps = selection_sort(array_selection)
end_time_selection = time.perf_counter_ns()
duration_selection = end_time_selection - start_time_selection
# Сортировка Шелла
array_shell = array.copy()
start_time_shell = time.perf_counter_ns()
shell_comparisons, shell_swaps = shell_sort(array_shell)
end_time_shell = time.perf_counter_ns()
duration_shell = end_time_shell - start_time_selection
# Вывод результатов


print("Bubble Sort")
print("Theoretical complexity: O(n^2)")
print("Number of comparisons:", bubble_comparisons)
print("Number of swaps:", bubble_swaps)
print("Duration:", duration_bubble, "ns")
print()

print("Insertion Sort")
print("Theoretical complexity: O(n^2)")
print("Number of comparisons:", insertion_comparisons)
print("Number of swaps:", insertion_swaps)
print("Duration:", duration_insertion, "ns")
print()

print("Selection Sort")
print("Theoretical complexity: O(n^2)")
print("Number of comparisons:", selection_comparisons)
print("Number of swaps:", selection_swaps)
print("Duration:", duration_selection, "ns")
print()

print("Shell Sort")
print("Theoretical complexity: O(n^(3/2))")
print("Number of comparisons:", shell_comparisons)
print("Number of swaps:", shell_swaps)
print("Duration:", duration_shell, "ns")
print()

