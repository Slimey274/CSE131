# quicksort_module.py

def segregate(data, i_start, i_end):
    pivot = data[i_end]
    i = i_start - 1

    for middle in range(i_start, i_end):
        if data[middle] <= pivot:
            i += 1
            data[i], data[middle] = data[middle], data[i]

    data[i + 1], data[i_end] = data[i_end], data[i + 1]
    return i + 1

def sort_recursive(data, i_start, i_end):
    if i_start < i_end:
        pivot_index = segregate(data, i_start, i_end)
        sort_recursive(data, i_start, pivot_index - 1)
        sort_recursive(data, pivot_index + 1, i_end)

def quicksort(data):
    sort_recursive(data, 0, len(data) - 1)
    return data  # For convenience in testing
