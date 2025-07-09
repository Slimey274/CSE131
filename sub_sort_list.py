# 1. Name:
#      -Briant Woolley-
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      -This program is ment to sort through a list and put in order-
# 4. What was the hardest part? Be as specific as possible.
#      -I feel the hardest part of this prigram for me was getting the list to sort its self.
#       This was hard because i had to figure out hoe it would sort is self automaticly. This is what I felt was the most difficult for me -
# 5. How long did it take for you to complete the assignment?
#      -1:30-

import random

def generate_random_list(size=20, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]

def sublist_sort(lst, start, end):
    if start < 0 or end >= len(lst) or start > end:
        raise ValueError("Invalid start or end index")

    # Sort the sublist in-place
    sub = lst[start:end + 1]
    sub.sort()

    # Update original list with sorted sublist
    return lst[:start] + sub + lst[end + 1:]

# Test cases

def test_middle_sublist():
    lst = [9, 3, 7, 1, 5, 8, 2, 4, 6, 0]
    result = sublist_sort(lst[:], 2, 6)
    assert result == [9, 3, 1, 2, 5, 7, 8, 4, 6, 0]

def test_full_list():
    lst = [10, 2, 5, 8, 1]
    result = sublist_sort(lst[:], 0, 4)
    assert result == [1, 2, 5, 8, 10]

def test_single_element():
    lst = [6, 3, 9, 2, 5]
    result = sublist_sort(lst[:], 3, 3)
    assert result == [6, 3, 9, 2, 5]

def test_already_sorted_sublist():
    lst = [4, 7, 1, 3, 6]
    result = sublist_sort(lst[:], 2, 4)
    assert result == [4, 7, 1, 3, 6]

def test_invalid_start_greater_than_end():
    try:
        sublist_sort([5, 2, 8, 1, 7], 4, 2)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_invalid_negative_index():
    try:
        sublist_sort([1, 2, 3], -1, 2)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_index_out_of_range():
    try:
        sublist_sort([1, 2, 3], 0, 5)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def run_all_tests():
    test_middle_sublist()
    test_full_list()
    test_single_element()
    test_already_sorted_sublist()
    test_invalid_start_greater_than_end()
    test_invalid_negative_index()
    test_index_out_of_range()
    print("All tests passed successfully.")

def main():
    run_all_tests()
    numbers = generate_random_list()
    print("Original list:")
    print(numbers)

    try:
        start = int(input("Enter the start index of the sublist to sort (0-19): "))
        end = int(input("Enter the end index of the sublist to sort (0-19): "))
        
        sorted_list = sublist_sort(numbers, start, end)

        print(f"\nSorted sublist (indices {start} to {end}):")
        print(sorted_list)

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
