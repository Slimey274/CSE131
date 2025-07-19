# 1. Name:
#      -Briant Woolley-
# 2. Assignment Name:
#      Lab 13 : Segregation Sort Program
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-
import random

data = []

def segregate(i_start, i_end):
    """
    Segregate or partition the list between indices i_start and i_end.
    
    This function rearranges elements so that those less than a pivot come before it,
    and those greater come after.
    
    Parameters:
        i_start (int): The starting index of the segment to be partitioned.
        i_end (int): The ending index of the segment to be partitioned.
    
    Returns:
        int: The index of the pivot after partitioning.
    """
    global data
    pivot = data[i_end]
    i = i_start -1
    print(f"\nPartitioning from index {i_start} to {i_end} with pivot {pivot}")

    for middle in range(i_start, i_end):
        if data[middle] <= pivot:
            i += 1
            data[i], data[middle] = data[middle], data[i]
            print(f"Swapped data[{i}] and data[{middle}]: {data}")
        else:
            print(f"No swap for data [{middle}] ({data[middle]}) > pivot ({pivot})")

    data[i + 1], data[i_end] = data[i_end], data[i + 1]
    print(f"Moved pivot to index {i + 1}: {data}")
    return i + 1

def sort_recursive(i_start, i_end):
    """
    Recursively sort the list using a divide-and-conquer approach.
    
    Parameters:
        i_start (int): The starting index of the segment to sort.
        i_end (int): The ending index of the segment to sort.
    """
    if i_start < i_end:
        print(f"\nRecursively sorting: start={i_start}, end={i_end}")
        pivot_index = segregate(i_start, i_end)
        print(f"Pivot positioned at index {pivot_index}, now sorting sublists")
        sort_recursive(i_start, pivot_index - 1)
        sort_recursive(pivot_index + 1, i_end)
    else:
        if i_start == i_end:
            print(f"Single element at index {i_start}, no action needed")
        else:
            print(f"No elements to sort between index {i_start} and {i_end}")

def sort():
    """
    Public entry point to sort the entire list.
    
    Typically, this function initializes the recursive sorting by 
    calling sort_recursive with the full range of the list.
    """
    global data
    print("\nStarting full sort...\n")
    sort_recursive(0, len(data) - 1)

def read():
    """
    Read or generate the list to be sorted.
    
    This function is responsible for obtaining the list—either from user input,
    file, or hardcoded for testing—and returning it.
    
    Returns:
        list: The list of items to be sorted.
    """
    global data
    data = [random.randint(0,99) for _ in range(20)]
    return data
    # print("Unsorted List:", data)

def main():
    """
    Main function to drive the program.
    
    This function orchestrates reading the data, sorting it, 
    and then displaying or using the result.
    """
    print('Unsorted list', read())
    sort()
    print("Sorted list:", data)
if __name__ == "__main__":
    main()